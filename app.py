from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import sqlite3
import os
from datetime import datetime, timedelta
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Database path
DB_PATH = os.path.join(os.path.dirname(__file__), 'hotel.db')

# Initialize database
def init_db():
    """Initialize database with required tables"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Customers table
    c.execute('''CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ref_id TEXT UNIQUE,
        name TEXT NOT NULL,
        email TEXT,
        phone TEXT,
        address TEXT,
        id_proof TEXT,
        id_number TEXT,
        nationality TEXT,
        gender TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    
    # Rooms table
    c.execute('''CREATE TABLE IF NOT EXISTS rooms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_number TEXT UNIQUE NOT NULL,
        room_type TEXT NOT NULL,
        price REAL NOT NULL,
        status TEXT DEFAULT 'Available',
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    
    # Bookings table
    c.execute('''CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        room_id INTEGER,
        check_in DATE NOT NULL,
        check_out DATE NOT NULL,
        total_price REAL,
        status TEXT DEFAULT 'Active',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(customer_id) REFERENCES customers(id),
        FOREIGN KEY(room_id) REFERENCES rooms(id)
    )''')

    # Seed a few default rooms if the database is empty so the UI has room options.
    c.execute('SELECT COUNT(*) FROM rooms')
    if c.fetchone()[0] == 0:
        default_rooms = [
            ('101', 'Standard', 100.0, 'Comfortable standard room'),
            ('102', 'Deluxe', 150.0, 'Spacious deluxe room'),
            ('103', 'Suite', 220.0, 'Luxury suite')
        ]
        c.executemany(
            'INSERT INTO rooms (room_number, room_type, price, description) VALUES (?, ?, ?, ?)',
            default_rooms
        )

    # Seed a default customer if the database has no customers.
    c.execute('SELECT COUNT(*) FROM customers')
    if c.fetchone()[0] == 0:
        c.execute('''INSERT INTO customers
                    (id, ref_id, name, email, phone, address, id_proof, id_number, nationality, gender)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (100, 'CUST_DEMO', 'Demo Guest', 'demo@example.com', '0000000000', 'Demo Address', 'Passport', 'DEMO123', 'Demo', 'Other'))
    
    conn.commit()
    conn.close()

# Initialize database on startup
init_db()

@app.route('/')
def index():
    """Dashboard page"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('SELECT COUNT(*) FROM customers')
    total_customers = c.fetchone()[0]
    
    c.execute('SELECT COUNT(*) FROM rooms')
    total_rooms = c.fetchone()[0]
    
    c.execute("SELECT COUNT(*) FROM rooms WHERE status='Available'")
    available_rooms = c.fetchone()[0]
    
    c.execute("SELECT COUNT(*) FROM bookings WHERE status='Active'")
    active_bookings = c.fetchone()[0]
    
    conn.close()
    
    return render_template('index.html', 
                         total_customers=total_customers,
                         total_rooms=total_rooms,
                         available_rooms=available_rooms,
                         active_bookings=active_bookings)

@app.route('/customers')
def customers():
    """Customers management page"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM customers ORDER BY created_at DESC')
    customers_list = c.fetchall()
    conn.close()
    return render_template('customers.html', customers=customers_list)

@app.route('/api/customers', methods=['POST'])
def add_customer():
    """Add new customer"""
    data = request.json
    
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        ref_id = f"CUST_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        c.execute('''INSERT INTO customers 
                    (ref_id, name, email, phone, address, id_proof, id_number, nationality, gender)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                 (ref_id, data['name'], data['email'], data['phone'], 
                  data['address'], data['id_proof'], data['id_number'], 
                  data['nationality'], data['gender']))
        
        conn.commit()
        customer_id = c.lastrowid
        conn.close()
        
        return jsonify({'success': True, 'customer_id': customer_id, 'ref_id': ref_id})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/rooms')
def rooms():
    """Rooms management page"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM rooms ORDER BY room_number')
    rooms_list = c.fetchall()
    conn.close()
    return render_template('rooms.html', rooms=rooms_list)

@app.route('/api/rooms', methods=['POST'])
def add_room():
    """Add new room"""
    data = request.json
    
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        c.execute('''INSERT INTO rooms 
                    (room_number, room_type, price, description)
                    VALUES (?, ?, ?, ?)''',
                 (data['room_number'], data['room_type'], data['price'], data['description']))
        
        conn.commit()
        conn.close()
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/bookings')
def bookings():
    """Bookings page"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''SELECT b.id, b.customer_id, b.room_id, b.check_in, b.check_out, b.total_price, b.status, b.created_at,
                 COALESCE(c.name, 'Unknown Customer') AS customer_name,
                 COALESCE(r.room_number, 'N/A') AS room_number,
                 COALESCE(r.room_type, 'N/A') AS room_type
                 FROM bookings b
                 LEFT JOIN customers c ON b.customer_id = c.id
                 LEFT JOIN rooms r ON b.room_id = r.id
                 ORDER BY b.created_at DESC''')
    bookings_list = c.fetchall()
    conn.close()
    return render_template('bookings.html', bookings=bookings_list)

@app.route('/api/bookings', methods=['POST'])
def create_booking():
    """Create new booking"""
    data = request.json
    
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        # Calculate total price
        check_in = datetime.strptime(data['check_in'], '%Y-%m-%d')
        check_out = datetime.strptime(data['check_out'], '%Y-%m-%d')
        nights = (check_out - check_in).days
        
        c.execute('SELECT price FROM rooms WHERE id = ?', (data['room_id'],))
        room_price = c.fetchone()[0]
        total_price = room_price * nights
        
        # Create booking
        c.execute('''INSERT INTO bookings 
                    (customer_id, room_id, check_in, check_out, total_price)
                    VALUES (?, ?, ?, ?, ?)''',
                 (data['customer_id'], data['room_id'], data['check_in'], 
                  data['check_out'], total_price))
        
        # Update room status
        c.execute('UPDATE rooms SET status = ? WHERE id = ?', ('Booked', data['room_id']))
        
        conn.commit()
        conn.close()
        
        return jsonify({'success': True, 'total_price': total_price})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/available-rooms')
def get_available_rooms():
    """Get rooms for the booking form"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, room_number, room_type, price, status FROM rooms ORDER BY room_number")
    rooms_list = c.fetchall()
    conn.close()
    
    return jsonify({
        'rooms': [{'id': r[0], 'number': r[1], 'type': r[2], 'price': r[3], 'status': r[4]} for r in rooms_list]
    })

# Customer API endpoints
@app.route('/api/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    """Get customer details"""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('SELECT * FROM customers WHERE id = ?', (customer_id,))
        customer = c.fetchone()
        conn.close()
        
        if customer:
            return jsonify({'success': True, 'customer': {
                'id': customer[0], 'ref_id': customer[1], 'name': customer[2],
                'email': customer[3], 'phone': customer[4], 'address': customer[5],
                'id_proof': customer[6], 'id_number': customer[7], 
                'nationality': customer[8], 'gender': customer[9]
            }})
        return jsonify({'success': False, 'error': 'Customer not found'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    """Update customer"""
    data = request.json
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''UPDATE customers 
                    SET name=?, email=?, phone=?, address=?, id_proof=?, id_number=?, nationality=?, gender=?
                    WHERE id=?''',
                 (data['name'], data['email'], data['phone'], data['address'],
                  data['id_proof'], data['id_number'], data['nationality'], data['gender'], customer_id))
        conn.commit()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    """Delete customer"""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('DELETE FROM customers WHERE id = ?', (customer_id,))
        conn.commit()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# Room API endpoints
@app.route('/api/rooms/<int:room_id>', methods=['GET'])
def get_room(room_id):
    """Get room details"""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('SELECT * FROM rooms WHERE id = ?', (room_id,))
        room = c.fetchone()
        conn.close()
        
        if room:
            return jsonify({'success': True, 'room': {
                'id': room[0], 'room_number': room[1], 'room_type': room[2],
                'price': room[3], 'status': room[4], 'description': room[5]
            }})
        return jsonify({'success': False, 'error': 'Room not found'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/rooms/<int:room_id>', methods=['PUT'])
def update_room(room_id):
    """Update room"""
    data = request.json
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''UPDATE rooms 
                    SET room_number=?, room_type=?, price=?, description=?, status=?
                    WHERE id=?''',
                 (data['room_number'], data['room_type'], data['price'], 
                  data['description'], data['status'], room_id))
        conn.commit()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/rooms/<int:room_id>', methods=['DELETE'])
def delete_room(room_id):
    """Delete room"""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('DELETE FROM rooms WHERE id = ?', (room_id,))
        conn.commit()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# Booking API endpoints
@app.route('/api/bookings/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    """Get booking details"""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''SELECT b.id, b.customer_id, b.room_id, b.check_in, b.check_out, b.total_price, b.status, b.created_at,
                     COALESCE(c.name, 'Unknown Customer') AS customer_name,
                     COALESCE(r.room_number, 'N/A') AS room_number,
                     COALESCE(r.room_type, 'N/A') AS room_type
                     FROM bookings b
                     LEFT JOIN customers c ON b.customer_id = c.id
                     LEFT JOIN rooms r ON b.room_id = r.id
                     WHERE b.id = ?''', (booking_id,))
        booking = c.fetchone()
        conn.close()
        
        if booking:
            return jsonify({'success': True, 'booking': {
                'id': booking[0], 'customer_id': booking[1], 'room_id': booking[2],
                'check_in': booking[3], 'check_out': booking[4], 'total_price': booking[5],
                'status': booking[6], 'customer_name': booking[8], 'room_number': booking[9], 'room_type': booking[10]
            }})
        return jsonify({'success': False, 'error': 'Booking not found'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/bookings/<int:booking_id>', methods=['PUT'])
def update_booking(booking_id):
    """Update booking"""
    data = request.json
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''UPDATE bookings 
                    SET status=?
                    WHERE id=?''',
                 (data['status'], booking_id))
        conn.commit()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/bookings/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    """Delete booking and free up room"""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        # Get room_id from booking
        c.execute('SELECT room_id FROM bookings WHERE id = ?', (booking_id,))
        result = c.fetchone()
        
        if result:
            room_id = result[0]
            # Delete booking
            c.execute('DELETE FROM bookings WHERE id = ?', (booking_id,))
            # Update room status back to Available
            c.execute('UPDATE rooms SET status = ? WHERE id = ?', ('Available', room_id))
        
        conn.commit()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
