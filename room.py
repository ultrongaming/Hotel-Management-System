from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
from time import strftime
from datetime import datetime
import os
import sqlite3
import mysql.connector


class RoomBooking:
    def __init__(self, root):   # ✅ Proper __init__
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1295x550+230+220")

        # ================ variables =================
        self.var_contact = StringVar()
        self.var_cheak_in = StringVar()
        self.var_cheak_out = StringVar()
        self.var_room_type = StringVar()
        self.var_room_available = StringVar()
        self.var_meal = StringVar()
        self.var_no_of_days = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        # ============== title =================
        lbl_title = Label(
            self.root,
            text="ROOM BOOKING DETAILS",
            font=("times new roman", 18, "bold"),
            bg="black",
            fg="gold",
            bd=4,
            relief=RIDGE
        )
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # =================logo=======================
        try:
            img2 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel Management System\hotel images\logohotel.png")
            img2 = img2.resize((100, 40), Image.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)
            lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
            lblimg.place(x=5, y=2, width=100, height=40)
        except Exception:
            lblimg = Label(self.root, text="LOGO", bd=0, relief=RIDGE)
            lblimg.place(x=5, y=2, width=100, height=40)

        # ====================labelframe=====================
        labelframeleft = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="Room Booking Details",
            font=("arial", 12, "bold"),
            fg="black"
        )
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ===============labels AND entrys=================
        # customer contact
        lbl_cust_contact = Label(
            labelframeleft,
            text="Customer Contact",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6
        )
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        entry_contact = ttk.Entry(
            labelframeleft,
            textvariable=self.var_contact,
            font=("arial", 13, "bold"),
            width=20
        )
        entry_contact.grid(row=0, column=1, sticky=W)

        btnFetchData = Button(
            labelframeleft,
            command=self.Fetch_contact,
            text="Fetch Data",
            font=("arial", 9, "bold"),
            bg="black",
            fg="gold",
            width=10
        )
        btnFetchData.place(x=335, y=4)

        # Cheak_in date
        cheak_in_date = Label(
            labelframeleft,
            font=("arial", 12, "bold"),
            text="Cheak_in Date:",
            padx=2,
            pady=6
        )
        cheak_in_date.grid(row=1, column=0, sticky=W)
        txtcheck_in_date = ttk.Entry(
            labelframeleft,
            textvariable=self.var_cheak_in,
            font=("arial", 13, "bold"),
            width=29
        )
        txtcheck_in_date.grid(row=1, column=1)

        # Cheak_out Date
        lbl_cheak_out = Label(
            labelframeleft,
            font=("arial", 12, "bold"),
            text="Cheak_out Date:",
            padx=2,
            pady=6
        )
        lbl_cheak_out.grid(row=2, column=0, sticky=W)
        txt_cheak_out = ttk.Entry(
            labelframeleft,
            textvariable=self.var_cheak_out,
            font=("arial", 13, "bold"),
            width=29
        )
        txt_cheak_out.grid(row=2, column=1)

        # Room type
        lbl_room_type = Label(
            labelframeleft,
            font=("arial", 12, "bold"),
            text="Room Type:",
            padx=2,
            pady=6
        )
        lbl_room_type.grid(row=3, column=0, sticky=W)

        combo_room_type = ttk.Combobox(
            labelframeleft,
            textvariable=self.var_room_type,
            font=("arial", 13, "bold"),
            width=27,
            state="readonly"
        )
        combo_room_type["value"] = ("Single", "Double", "Luxury")
        combo_room_type.current(0)
        combo_room_type.grid(row=3, column=1)

        # Available room
        lblRoomAvailable = Label(
            labelframeleft,
            font=("arial", 12, "bold"),
            text="Available Room:",
            padx=2,
            pady=6
        )
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        txtRoomAvailable = ttk.Entry(
            labelframeleft,
            textvariable=self.var_room_available,
            font=("arial", 13, "bold"),
            width=29
        )
        txtRoomAvailable.grid(row=4, column=1)

        # Meal
        lblMeal = Label(
            labelframeleft,
            font=("arial", 12, "bold"),
            text="Meal:",
            padx=2,
            pady=6
        )
        lblMeal.grid(row=5, column=0, sticky=W)
        txtMeal = ttk.Entry(
            labelframeleft,
            textvariable=self.var_meal,
            font=("arial", 13, "bold"),
            width=29
        )
        txtMeal.grid(row=5, column=1)

        # No of days
        lblNoOfDays = Label(
            labelframeleft,
            font=("arial", 12, "bold"),
            text="No of Days:",
            padx=2,
            pady=6
        )
        lblNoOfDays.grid(row=6, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(
            labelframeleft,
            textvariable=self.var_no_of_days,
            font=("arial", 13, "bold"),
            width=29
        )
        txtNoOfDays.grid(row=6, column=1)

        # Paid Tax
        lblPaidTax = Label(
            labelframeleft,
            font=("arial", 12, "bold"),
            text="Paid Tax:",
            padx=2,
            pady=6
        )
        lblPaidTax.grid(row=7, column=0, sticky=W)
        txtPaidTax = ttk.Entry(
            labelframeleft,
            textvariable=self.var_paidtax,
            font=("arial", 13, "bold"),
            width=29
        )
        txtPaidTax.grid(row=7, column=1)

        # Sub Total
        lblSubTotal = Label(
            labelframeleft,
            font=("arial", 12, "bold"),
            text="Sub Total:",
            padx=2,
            pady=6
        )
        lblSubTotal.grid(row=8, column=0, sticky=W)
        txtSubTotal = ttk.Entry(
            labelframeleft,
            textvariable=self.var_actualtotal,
            font=("arial", 13, "bold"),
            width=29
        )
        txtSubTotal.grid(row=8, column=1)

        # Total Cost
        lblTotalCost = Label(
            labelframeleft,
            font=("arial", 12, "bold"),
            text="Total Cost:",
            padx=2,
            pady=6
        )
        lblTotalCost.grid(row=9, column=0, sticky=W)
        txtTotalCost = ttk.Entry(
            labelframeleft,
            textvariable=self.var_total,
            font=("arial", 13, "bold"),
            width=29
        )
        txtTotalCost.grid(row=9, column=1)

        # Bill Button
        btnBill = Button(
            labelframeleft,
            text="Bill",
            command=self.total,
            font=("arial", 12, "bold"),
            bg="black",
            fg="gold",
            width=10
        )
        btnBill.grid(row=10, column=0, pady=8, sticky=W)

        # ====================buttons=====================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(
            btn_frame,
            text="Add",
            command=self.add_data,
            font=("arial", 12, "bold"),
            bg="black",
            fg="gold",
            width=9
        )
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(
            btn_frame,
            text="Update",
            command=self.update_data,
            font=("arial", 12, "bold"),
            bg="black",
            fg="gold",
            width=9
        )
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(
            btn_frame,
            text="Delete",
            command=self.delete_data,
            font=("arial", 12, "bold"),
            bg="black",
            fg="gold",
            width=9
        )
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(
            btn_frame,
            text="Reset",
            command=self.reset_data,
            font=("arial", 12, "bold"),
            bg="black",
            fg="gold",
            width=9
        )
        btnReset.grid(row=0, column=3, padx=1)

        # ====================Right Side Image=====================
        try:
            img3 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel Management System\hotel images\bed.jpg")
            img3 = img3.resize((545, 295), Image.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)
            lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
            lblimg.place(x=750, y=55, width=545, height=295)
        except Exception:
            lblimg = Label(self.root, text="BED IMAGE", bd=0, relief=RIDGE)
            lblimg.place(x=750, y=55, width=545, height=295)

        # ====================table frame=====================
        Table_Frame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="View Details And Search System",
            font=("arial", 12, "bold"),
            fg="black"
        )
        Table_Frame.place(x=435, y=280, width=860, height=260)

        lblSearchby = Label(
            Table_Frame,
            font=("arial", 12, "bold"),
            text="Search By:",
            bg="red",
            fg="white"
        )
        lblSearchby.grid(row=0, column=0, sticky=W, padx=2)

        self.var_searchby = StringVar()
        combo_Search = ttk.Combobox(
            Table_Frame,
            font=("arial", 12, "bold"),
            width=27,
            state="readonly",
            textvariable=self.var_searchby
        )
        combo_Search["values"] = ("Contact", "Room")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1)

        self.var_searchtxt = StringVar()
        txtSearch = ttk.Entry(
            Table_Frame,
            textvariable=self.var_searchtxt,
            font=("arial", 13, "bold"),
            width=24
        )
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(
            Table_Frame,
            text="Search",
            command=self.search_data,
            font=("arial", 12, "bold"),
            bg="black",
            fg="gold",
            width=10
        )
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(
            Table_Frame,
            text="Show All",
            command=self.fetch_data,
            font=("arial", 12, "bold"),
            bg="black",
            fg="gold",
            width=10
        )
        btnShowAll.grid(row=0, column=4, padx=1)

        # ===================show table data==================
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(
            details_table,
            columns=("contact", "cheakin", "cheakout", "roomtype", "roomavailable", "meal", "noofdays"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        # ===== Headings =====
        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("cheakin", text="Cheak-in")
        self.room_table.heading("cheakout", text="Cheak-out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noofdays", text="No of Days")

        self.room_table["show"] = "headings"

        # ===== Column Widths =====
        self.room_table.column("contact", width=100)
        self.room_table.column("cheakin", width=100)
        self.room_table.column("cheakout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noofdays", width=100)

        self.room_table.pack(fill=BOTH, expand=1)

        # bind row selection
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

        # connect DB and load data
        self.connect_db()
        self.fetch_data()

    # ============= Database Helpers ==============
    def connect_db(self):
        """
        Connects to MySQL and ensures room_booking table exists.
        Falls back to SQLite hotel.db if MySQL not available.
        """
        db_host = os.environ.get("DB_HOST", "localhost")
        db_user = os.environ.get("DB_USER", "root")
        db_pass = os.environ.get("DB_PASS", "")
        try:
            if db_user:
                self.conn = mysql.connector.connect(
                    host=db_host,
                    user=db_user,
                    password=db_pass,
                    auth_plugin='mysql_native_password'
                )
                self.cursor = self.conn.cursor()
                self.db_type = 'mysql'
                # create DB if not exists
                self.cursor.execute("CREATE DATABASE IF NOT EXISTS hotel_db")
                self.cursor.execute("USE hotel_db")
                # create table
                create_table_query = """
                CREATE TABLE IF NOT EXISTS room_booking (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    contact VARCHAR(50),
                    checkin VARCHAR(50),
                    checkout VARCHAR(50),
                    room_type VARCHAR(50),
                    room_available VARCHAR(50),
                    meal VARCHAR(100),
                    no_of_days VARCHAR(50),
                    paid_tax VARCHAR(50),
                    sub_total VARCHAR(50),
                    total VARCHAR(50)
                )
                """
                self.cursor.execute(create_table_query)
                self.conn.commit()
                return
        except Exception:
            pass

        # SQLite fallback
        try:
            db_path = os.path.join(os.path.dirname(__file__), 'hotel.db')
            self.conn = sqlite3.connect(db_path)
            self.cursor = self.conn.cursor()
            self.db_type = 'sqlite'
            create_table_sqlite = """
            CREATE TABLE IF NOT EXISTS room_booking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contact TEXT,
                checkin TEXT,
                checkout TEXT,
                room_type TEXT,
                room_available TEXT,
                meal TEXT,
                no_of_days TEXT,
                paid_tax TEXT,
                sub_total TEXT,
                total TEXT
            )
            """
            self.cursor.execute(create_table_sqlite)
            self.conn.commit()
        except sqlite3.Error as err:
            messagebox.showerror("Database Error", f"Error connecting/creating DB:\n{err}")
            self.root.destroy()

    def db_execute(self, query, params=None, commit=False):
        """Execute a query using active DB connection. Converts %s to ? for sqlite."""
        if params is None:
            params = ()
        q = query
        try:
            if getattr(self, 'db_type', None) == 'sqlite':
                q = query.replace('%s', '?')
            self.cursor.execute(q, params)
            if commit:
                self.conn.commit()
        except Exception as err:
            raise

    # ============= CRUD Operations ==============
    def add_data(self):
        if self.var_contact.get() == "" or self.var_cheak_in.get() == "":
            messagebox.showerror("Error", "Contact and Check-in Date are required")
            return
        try:
            query = """
            INSERT INTO room_booking
            (contact, checkin, checkout, room_type, room_available, meal,
             no_of_days, paid_tax, sub_total, total)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            values = (
                self.var_contact.get(),
                self.var_cheak_in.get(),
                self.var_cheak_out.get(),
                self.var_room_type.get(),
                self.var_room_available.get(),
                self.var_meal.get(),
                self.var_no_of_days.get(),
                self.var_paidtax.get(),
                self.var_actualtotal.get(),
                self.var_total.get()
            )
            self.db_execute(query, values, commit=True)
            messagebox.showinfo("Success", "Room booking added successfully")
            self.fetch_data()
            self.reset_data()
        except Exception as err:
            messagebox.showerror("Error", f"Database error: {err}")

    def fetch_data(self):
        # clear table
        for item in self.room_table.get_children():
            self.room_table.delete(item)
        try:
            self.db_execute(
                "SELECT contact, checkin, checkout, room_type, room_available, meal, no_of_days FROM room_booking"
            )
            rows = self.cursor.fetchall()
            for row in rows:
                self.room_table.insert('', END, values=row)
        except Exception as err:
            messagebox.showerror("Error", f"Failed fetching data: {err}")

    def get_cursor(self, event=""):
        # get cursor value from treeview and set to form
        selected_row = self.room_table.focus()
        data = self.room_table.item(selected_row)
        row = data.get('values')
        if row:
            self.var_contact.set(row[0])
            self.var_cheak_in.set(row[1])
            self.var_cheak_out.set(row[2])
            self.var_room_type.set(row[3])
            self.var_room_available.set(row[4])
            self.var_meal.set(row[5])
            self.var_no_of_days.set(row[6])
            # paidtax, subtotal, total are not shown in table; they stay as is

    def update_data(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please select a record to update")
            return
        try:
            update_query = """
            UPDATE room_booking
            SET checkin=%s, checkout=%s, room_type=%s, room_available=%s,
                meal=%s, no_of_days=%s, paid_tax=%s, sub_total=%s, total=%s
            WHERE contact=%s
            """
            values = (
                self.var_cheak_in.get(),
                self.var_cheak_out.get(),
                self.var_room_type.get(),
                self.var_room_available.get(),
                self.var_meal.get(),
                self.var_no_of_days.get(),
                self.var_paidtax.get(),
                self.var_actualtotal.get(),
                self.var_total.get(),
                self.var_contact.get()
            )
            self.db_execute(update_query, values, commit=True)
            messagebox.showinfo("Success", "Record updated successfully")
            self.fetch_data()
            self.reset_data()
        except Exception as err:
            messagebox.showerror("Error", f"Failed to update: {err}")

    def delete_data(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please select a record to delete")
            return
        confirm = messagebox.askyesno("Confirm Delete", "Do you really want to delete this booking?")
        if confirm:
            try:
                self.db_execute(
                    "DELETE FROM room_booking WHERE contact=%s",
                    (self.var_contact.get(),),
                    commit=True
                )
                messagebox.showinfo("Deleted", "Record deleted successfully")
                self.fetch_data()
                self.reset_data()
            except Exception as err:
                messagebox.showerror("Error", f"Failed to delete: {err}")

    def reset_data(self):
        self.var_contact.set("")
        self.var_cheak_in.set("")
        self.var_cheak_out.set("")
        self.var_room_type.set("Single")
        self.var_room_available.set("")
        self.var_meal.set("")
        self.var_no_of_days.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

    def search_data(self):
        search_by = self.var_searchby.get()
        txt = self.var_searchtxt.get()
        if txt == "":
            messagebox.showerror("Error", "Enter search text")
            return
        try:
            for item in self.room_table.get_children():
                self.room_table.delete(item)

            if search_by == "Contact":
                self.db_execute(
                    "SELECT contact, checkin, checkout, room_type, room_available, meal, no_of_days "
                    "FROM room_booking WHERE contact LIKE %s",
                    (f"%{txt}%",)
                )
            else:  # Room
                self.db_execute(
                    "SELECT contact, checkin, checkout, room_type, room_available, meal, no_of_days "
                    "FROM room_booking WHERE room_available LIKE %s",
                    (f"%{txt}%",)
                )
            rows = self.cursor.fetchall()
            for row in rows:
                self.room_table.insert('', END, values=row)
        except Exception as err:
            messagebox.showerror("Error", f"Search failed: {err}")

    # =================== Fetch customer data by contact ===================
    def Fetch_contact(self):
        if self.var_contact.get().strip() == "":
            messagebox.showerror("Error", "Please enter contact number", parent=self.root)
            return

        contact = self.var_contact.get().strip()

        conn = None
        my_cursor = None
        row = None

        # Try MySQL first using environment or defaults
        mysql_host = os.environ.get("DB_HOST", "localhost")
        mysql_user = os.environ.get("DB_USER", "root")
        mysql_pass = os.environ.get("DB_PASS", "")
        mysql_db = os.environ.get("DB_NAME", "hotel_db")

        try:
            conn = mysql.connector.connect(
                host=mysql_host,
                user=mysql_user,
                password=mysql_pass,
                database=mysql_db,
                auth_plugin='mysql_native_password'
            )
            my_cursor = conn.cursor()
            query = "SELECT name, gender, email, nationality, address FROM hotel_customer WHERE mobile=%s"
            my_cursor.execute(query, (contact,))
            row = my_cursor.fetchone()
        except Exception:
            # Fall back to SQLite
            try:
                if my_cursor:
                    try:
                        my_cursor.close()
                    except Exception:
                        pass
                if conn:
                    try:
                        conn.close()
                    except Exception:
                        pass

                db_path = os.path.join(os.path.dirname(__file__), 'hotel.db')
                conn = sqlite3.connect(db_path)
                my_cursor = conn.cursor()
                query = "SELECT name, gender, email, nationality, address FROM hotel_customer WHERE mobile=?"
                my_cursor.execute(query, (contact,))
                row = my_cursor.fetchone()
            except sqlite3.Error as err:
                messagebox.showerror("Database Error", f"Could not open local DB:\n{err}", parent=self.root)
                return

        try:
            if row is None:
                messagebox.showerror("Error", "This contact number not found", parent=self.root)
                return

            name, gender, email, nationality, address = row

            if hasattr(self, "showDataframe") and self.showDataframe.winfo_exists():
                self.showDataframe.destroy()

            self.showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
            self.showDataframe.place(x=450, y=55, width=300, height=180)

            lblName = Label(self.showDataframe, text="Name:", font=("arial", 12, "bold"))
            lblName.place(x=0, y=0)
            lbl = Label(self.showDataframe, text=str(name), font=("arial", 12, "bold"))
            lbl.place(x=90, y=0)

            lblGender = Label(self.showDataframe, text="Gender:", font=("arial", 12, "bold"))
            lblGender.place(x=0, y=30)
            lbl2 = Label(self.showDataframe, text=str(gender), font=("arial", 12, "bold"))
            lbl2.place(x=90, y=30)

            lblEmail = Label(self.showDataframe, text="Email:", font=("arial", 12, "bold"))
            lblEmail.place(x=0, y=60)
            lbl3 = Label(self.showDataframe, text=str(email), font=("arial", 12, "bold"))
            lbl3.place(x=90, y=60)

            lblAddress = Label(self.showDataframe, text="Address:", font=("arial", 12, "bold"))
            lblAddress.place(x=0, y=90)
            lbl5 = Label(self.showDataframe, text=str(address), font=("arial", 12, "bold"))
            lbl5.place(x=90, y=90)

            lblNationality = Label(self.showDataframe, text="Nationality:", font=("arial", 12, "bold"))
            lblNationality.place(x=0, y=120)
            lbl4 = Label(self.showDataframe, text=str(nationality), font=("arial", 12, "bold"))
            lbl4.place(x=90, y=120)

        except Exception as e:
            messagebox.showerror("Query Error", f"An error occurred when fetching data:\n{e}", parent=self.root)
        finally:
            try:
                if my_cursor:
                    my_cursor.close()
            except Exception:
                pass
            try:
                if conn:
                    conn.close()
            except Exception:
                pass

    # =================== Total / Bill Calculation ===================
    def total(self):
        inDate_str = self.var_cheak_in.get()
        outDate_str = self.var_cheak_out.get()

        # validate dates
        try:
            inDate = datetime.strptime(inDate_str, "%d/%m/%Y")
            outDate = datetime.strptime(outDate_str, "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Error", "Please enter dates in DD/MM/YYYY format", parent=self.root)
            return

        noOfDays = (outDate - inDate).days
        if noOfDays <= 0:
            messagebox.showerror("Error", "Check-out date must be after check-in date", parent=self.root)
            return

        self.var_no_of_days.set(str(noOfDays))

        # Example price logic: Breakfast + Luxury
        if self.var_meal.get() == "Breakfast" and self.var_room_type.get() == "Luxury":
            room_cost_per_day = 700.0
            meal_cost_per_day = 300.0

            per_day_total = room_cost_per_day + meal_cost_per_day
            sub_total = noOfDays * per_day_total
            tax = sub_total * 0.09
            grand_total = sub_total + tax

            self.var_paidtax.set("Rs." + f"{tax:.2f}")
            self.var_actualtotal.set("Rs." + f"{sub_total:.2f}")
            self.var_total.set("Rs." + f"{grand_total:.2f}")


if __name__ == "__main__":
    root = Tk()
    obj = RoomBooking(root)
    root.mainloop()
