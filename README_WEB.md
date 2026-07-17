# EliteStay Hotel Management System - Web Edition 🏨

A modern, professional web-based Hotel Management System built with Flask, featuring a sleek UI for managing customers, rooms, and bookings.

## Features

✨ **Modern Professional Design**
- Responsive Bootstrap 5 interface
- Beautiful gradient styling with smooth animations
- Mobile-friendly layout
- Professional dashboard with real-time statistics

📊 **Core Features**
- Customer registration and management
- Room inventory management
- Booking system with price calculation
- Real-time availability tracking
- Professional data tables and forms

🎯 **User-Friendly Interface**
- Intuitive navigation
- Quick action buttons
- Modal forms for data entry
- Real-time cost estimation
- Status tracking with visual badges

## Project Structure

```
Hotel-Management-System-main/
├── app.py                      # Flask application backend
├── requirements.txt            # Python dependencies
├── hotel.db                    # SQLite database
├── config.py                   # Configuration settings
│
├── static/
│   ├── css/
│   │   └── style.css          # Professional styling
│   └── js/
│       └── main.js            # Frontend functionality
│
├── templates/
│   ├── base.html              # Base template
│   ├── index.html             # Dashboard
│   ├── customers.html         # Customer management
│   ├── rooms.html             # Room management
│   └── bookings.html          # Booking management
│
└── hotel images/              # Hotel branding images
```

## Setup Instructions

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python app.py
```

The application will start at: **http://localhost:5000**

### 3. Access the System

Open your browser and navigate to:
- **Dashboard**: http://localhost:5000/
- **Customers**: http://localhost:5000/customers
- **Rooms**: http://localhost:5000/rooms
- **Bookings**: http://localhost:5000/bookings

## Default Database

The system uses SQLite (`hotel.db`). The database is automatically created on first run with the required tables.

## Features Walkthrough

### 🏠 Dashboard
- Real-time statistics
- Total customers, rooms, available rooms, and active bookings
- Quick action buttons for all major functions

### 👥 Customer Management
- Add new customer with details
- View all customers in a professional table
- Customer reference ID auto-generated
- Support for ID proof tracking
- Contact information management

### 🛏️ Room Management
- Add rooms with type and pricing
- Visual room cards with status indicators
- Price per night management
- Room descriptions and amenities
- Available/Booked status tracking

### 📅 Booking Management
- Create new bookings
- Automatic price calculation based on stay duration
- Customer-to-room assignment
- Check-in and check-out date management
- Booking status tracking

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Database**: SQLite
- **Styling**: Custom CSS with gradient effects
- **Icons**: Bootstrap Icons

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Dashboard page |
| GET | `/customers` | Customers page |
| POST | `/api/customers` | Add new customer |
| GET | `/rooms` | Rooms page |
| POST | `/api/rooms` | Add new room |
| GET | `/bookings` | Bookings page |
| POST | `/api/bookings` | Create booking |
| GET | `/api/available-rooms` | Get available rooms |

## Styling Highlights

✨ **Professional Features**:
- Gradient backgrounds throughout
- Smooth hover animations
- Color-coded status badges
- Responsive design for all devices
- Shadow effects for depth
- Consistent typography and spacing

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers

## Future Enhancements

- User authentication and login system
- Email notifications
- Payment processing
- Advanced reporting
- Multi-language support
- Staff management
- Maintenance scheduling

## Notes

- Database file is stored locally in `hotel.db`
- Images should be placed in the `hotel images` folder
- All data is stored in SQLite format
- Application runs on development server (not for production)

## Support

For issues or feature requests, please contact the development team.

---

**Version**: 1.0  
**Last Updated**: 2024  
**License**: MIT
