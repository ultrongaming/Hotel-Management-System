from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import os
import sqlite3
import mysql.connector


class Cust_Win:
    def __init__(self, root):   # ✅ use __init__ so it runs correctly
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1295x550+230+220")

        # Variables (make them instance vars so methods can use them)
        self.var_ref = StringVar()
        self.var_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_idproof = StringVar()
        self.var_idnumber = StringVar()
        self.var_address = StringVar()

        # ==================title========
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS",
                          font=("times new roman", 18, "bold"),
                          bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # =================logo=======================
        img2 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel Management System\hotel images\logohotel.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        # ====================labelframe=====================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE,
                                    text="Customer Details", font=("arial", 12, "bold"), fg="black")
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ==================labels and entrys============
        # customer ref
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref",
                             font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        entry_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, font=("arial", 13, "bold"), width=29)
        entry_ref.grid(row=0, column=1)

        # Customer Name
        cname = Label(labelframeleft, font=("arial", 12, "bold"),
                      text="Customer Name:", padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtcname = ttk.Entry(labelframeleft, textvariable=self.var_name, font=("arial", 13, "bold"), width=29)
        txtcname.grid(row=1, column=1)

        # Mother Name
        lblmname = Label(labelframeleft, font=("arial", 12, "bold"),
                         text="Mother Name:", padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)
        txtmname = ttk.Entry(labelframeleft, textvariable=self.var_mother, font=("arial", 13, "bold"), width=29)
        txtmname.grid(row=2, column=1)

        # Gender ComboBox
        label_gender = Label(labelframeleft, font=("arial", 12, "bold"),
                             text="Gender:", padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(labelframeleft, font=("arial", 12, "bold"),
                                    width=27, state="readonly", textvariable=self.var_gender)
        combo_gender["values"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # Postcode
        lblPostcode = Label(labelframeleft, font=("arial", 12, "bold"),
                            text="Postcode:", padx=2, pady=6)
        lblPostcode.grid(row=4, column=0, sticky=W)
        txtPostcode = ttk.Entry(labelframeleft, textvariable=self.var_post, font=("arial", 13, "bold"), width=29)
        txtPostcode.grid(row=4, column=1)

        # Mobile
        lblMobile = Label(labelframeleft, font=("arial", 12, "bold"),
                          text="Mobile:", padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)
        txtMobile = ttk.Entry(labelframeleft, textvariable=self.var_mobile, font=("arial", 13, "bold"), width=29)
        txtMobile.grid(row=5, column=1)

        # Email
        lblEmail = Label(labelframeleft, font=("arial", 12, "bold"),
                         text="Email:", padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)
        txtEmail = ttk.Entry(labelframeleft, textvariable=self.var_email, font=("arial", 13, "bold"), width=29)
        txtEmail.grid(row=6, column=1)

        # Nationality
        lblNationality = Label(labelframeleft, font=("arial", 12, "bold"),
                               text="Nationality:", padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)
        comboNationality = ttk.Combobox(labelframeleft, font=("arial", 12, "bold"),
                                        width=27, state="readonly", textvariable=self.var_nationality)
        comboNationality["values"] = ("Indian", "American", "British", "Other")
        comboNationality.current(0)
        comboNationality.grid(row=7, column=1)

        # ID Proof Type
        lblIdproof = Label(labelframeleft, font=("arial", 12, "bold"),
                           text="ID Proof Type:", padx=2, pady=6)
        lblIdproof.grid(row=8, column=0, sticky=W)
        comboIdproof = ttk.Combobox(labelframeleft, font=("arial", 12, "bold"),
                                    width=27, state="readonly", textvariable=self.var_idproof)
        comboIdproof["values"] = ("Aadhar Card", "Passport", "Driving License", "PAN Card")
        comboIdproof.current(0)
        comboIdproof.grid(row=8, column=1)

        # ID Number
        lblIdnumber = Label(labelframeleft, font=("arial", 12, "bold"),
                            text="ID Number:", padx=2, pady=6)
        lblIdnumber.grid(row=9, column=0, sticky=W)
        txtIdnumber = ttk.Entry(labelframeleft, textvariable=self.var_idnumber, font=("arial", 13, "bold"), width=29)
        txtIdnumber.grid(row=9, column=1)

        # Address
        lblAddress = Label(labelframeleft, font=("arial", 12, "bold"),
                           text="Address:", padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)
        txtAddress = ttk.Entry(labelframeleft, textvariable=self.var_address, font=("arial", 13, "bold"), width=29)
        txtAddress.grid(row=10, column=1)

        # ===========buttons=============
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.delete_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1)

        # ============tableframe=======================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE,
                                 text="View Details And Search System", font=("arial", 12, "bold"), fg="black")
        Table_Frame.place(x=435, y=50, width=860, height=490)

        lblSearchby = Label(Table_Frame, font=("arial", 12, "bold"), text="Search By:", bg="red", fg="white")
        lblSearchby.grid(row=0, column=0, sticky=W, padx=2)

        self.var_searchby = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, font=("arial", 12, "bold"),
                                    width=27, state="readonly", textvariable=self.var_searchby)
        combo_Search["values"] = ("Mobile", "Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1)

        self.var_searchtxt = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.var_searchtxt, font=("arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", command=self.search_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All", command=self.fetch_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        # ===================show table data==================
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, column=("ref", "name", "mother", "gender", "post", "mobile", "email",
                                                                      "nationality", "idproof", "idnumber", "address"),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref", text="Refer No")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("mother", text="Mother Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("post", text="PostCode")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("idproof", text="Id Proof")
        self.Cust_Details_Table.heading("idnumber", text="Id Number")
        self.Cust_Details_Table.heading("address", text="Address")

        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("mother", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("post", width=100)
        self.Cust_Details_Table.column("mobile", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("idproof", width=100)
        self.Cust_Details_Table.column("idnumber", width=100)
        self.Cust_Details_Table.column("address", width=100)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)

        # Bind the treeview select
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)

        # Initialize DB and fetch existing data
        self.connect_db()
        self.fetch_data()

    def connect_db(self):
        """
        Connects to MySQL and ensures database/table exist.
        Change the host/user/password values if necessary.
        """
        # Try MySQL first (configurable via environment variables), otherwise fall back to local SQLite
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
                # create database if not exists and use it
                self.cursor.execute("CREATE DATABASE IF NOT EXISTS hotel_db")
                self.cursor.execute("USE hotel_db")
                # create table for MySQL
                create_table_query = """
                CREATE TABLE IF NOT EXISTS hotel_customer (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    ref VARCHAR(100) UNIQUE,
                    name VARCHAR(255),
                    mother VARCHAR(255),
                    gender VARCHAR(50),
                    post VARCHAR(50),
                    mobile VARCHAR(50),
                    email VARCHAR(255),
                    nationality VARCHAR(100),
                    idproof VARCHAR(100),
                    idnumber VARCHAR(100),
                    address VARCHAR(500)
                )
                """
                self.cursor.execute(create_table_query)
                self.conn.commit()
                return
        except mysql.connector.Error:
            # if MySQL fails, we'll fall back to sqlite below
            pass

        # SQLite fallback
        try:
            db_path = os.path.join(os.path.dirname(__file__), 'hotel.db')
            self.conn = sqlite3.connect(db_path)
            self.cursor = self.conn.cursor()
            self.db_type = 'sqlite'
            # create table for SQLite (types adapted)
            create_table_sqlite = """
            CREATE TABLE IF NOT EXISTS hotel_customer (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ref TEXT UNIQUE,
                name TEXT,
                mother TEXT,
                gender TEXT,
                post TEXT,
                mobile TEXT,
                email TEXT,
                nationality TEXT,
                idproof TEXT,
                idnumber TEXT,
                address TEXT
            )
            """
            self.cursor.execute(create_table_sqlite)
            self.conn.commit()
        except sqlite3.Error as err:
            messagebox.showerror("Database Error", f"Error connecting/creating DB:\n{err}")
            self.root.destroy()

    def db_execute(self, query, params=None, commit=False):
        """Execute a query using the active DB connection.
        Converts %s placeholders to ? for sqlite.
        """
        if params is None:
            params = ()
        q = query
        try:
            if getattr(self, 'db_type', None) == 'sqlite':
                # convert %s -> ? for sqlite parameter style
                q = query.replace('%s', '?')
            self.cursor.execute(q, params)
            if commit:
                self.conn.commit()
        except Exception as err:
            raise

    def add_data(self):
        if self.var_ref.get() == "" or self.var_mobile.get() == "":
            messagebox.showerror("Error", "Customer Refer and Mobile are required")
            return
        try:
            query = "INSERT INTO hotel_customer (ref, name, mother, gender, post, mobile, email, nationality, idproof, idnumber, address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (
                self.var_ref.get(),
                self.var_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_idproof.get(),
                self.var_idnumber.get(),
                self.var_address.get()
            )
            self.db_execute(query, values, commit=True)
            messagebox.showinfo("Success", "Customer added successfully")
            self.fetch_data()
            self.reset_data()
        except (mysql.connector.IntegrityError, sqlite3.IntegrityError):
            messagebox.showerror("Error", "Reference number must be unique. Change Ref and try again.")
        except Exception as err:
            messagebox.showerror("Error", f"Database error: {err}")

    def fetch_data(self):
        # clear table
        for item in self.Cust_Details_Table.get_children():
            self.Cust_Details_Table.delete(item)
        try:
            self.db_execute("SELECT ref, name, mother, gender, post, mobile, email, nationality, idproof, idnumber, address FROM hotel_customer")
            rows = self.cursor.fetchall()
            for row in rows:
                self.Cust_Details_Table.insert('', END, values=row)
        except Exception as err:
            messagebox.showerror("Error", f"Failed fetching data: {err}")

    def get_cursor(self, event=""):
        # get cursor value from treeview and set to form
        selected_row = self.Cust_Details_Table.focus()
        data = self.Cust_Details_Table.item(selected_row)
        row = data.get('values')
        if row:
            self.var_ref.set(row[0])
            self.var_name.set(row[1])
            self.var_mother.set(row[2])
            self.var_gender.set(row[3])
            self.var_post.set(row[4])
            self.var_mobile.set(row[5])
            self.var_email.set(row[6])
            self.var_nationality.set(row[7])
            self.var_idproof.set(row[8])
            self.var_idnumber.set(row[9])
            self.var_address.set(row[10])

    def update_data(self):
        if self.var_ref.get() == "":
            messagebox.showerror("Error", "Please select a record to update")
            return
        try:
            update_query = """
            UPDATE hotel_customer SET name=%s, mother=%s, gender=%s, post=%s, mobile=%s, email=%s, nationality=%s, idproof=%s, idnumber=%s, address=%s
            WHERE ref=%s
            """
            values = (
                self.var_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_idproof.get(),
                self.var_idnumber.get(),
                self.var_address.get(),
                self.var_ref.get()
            )
            self.db_execute(update_query, values, commit=True)
            messagebox.showinfo("Success", "Record updated successfully")
            self.fetch_data()
            self.reset_data()
        except Exception as err:
            messagebox.showerror("Error", f"Failed to update: {err}")

    def delete_data(self):
        if self.var_ref.get() == "":
            messagebox.showerror("Error", "Please select a record to delete")
            return
        confirm = messagebox.askyesno("Confirm Delete", "Do you really want to delete this record?")
        if confirm:
            try:
                self.db_execute("DELETE FROM hotel_customer WHERE ref=%s", (self.var_ref.get(),), commit=True)
                messagebox.showinfo("Deleted", "Record deleted successfully")
                self.fetch_data()
                self.reset_data()
            except Exception as err:
                messagebox.showerror("Error", f"Failed to delete: {err}")

    def reset_data(self):
        self.var_ref.set("")
        self.var_name.set("")
        self.var_mother.set("")
        self.var_gender.set("Male")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_nationality.set("Indian")
        self.var_idproof.set("Aadhar Card")
        self.var_idnumber.set("")
        self.var_address.set("")

    def search_data(self):
        search_by = self.var_searchby.get()
        txt = self.var_searchtxt.get()
        if txt == "":
            messagebox.showerror("Error", "Enter search text")
            return
        try:
            for item in self.Cust_Details_Table.get_children():
                self.Cust_Details_Table.delete(item)

            if search_by == "Mobile":
                self.db_execute("SELECT ref, name, mother, gender, post, mobile, email, nationality, idproof, idnumber, address FROM hotel_customer WHERE mobile LIKE %s", (f"%{txt}%",))
            else:  # Ref
                self.db_execute("SELECT ref, name, mother, gender, post, mobile, email, nationality, idproof, idnumber, address FROM hotel_customer WHERE ref LIKE %s", (f"%{txt}%",))
            rows = self.cursor.fetchall()
            for row in rows:
                self.Cust_Details_Table.insert('', END, values=row)
        except Exception as err:
            messagebox.showerror("Error", f"Search failed: {err}")


if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
