from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
from customer import Cust_Win
import importlib
import os


class HotelManagementSystem:
    def __init__(self, root):   # ✅ fixed: use __init__ so it runs correctly
        self.root = root
        self.root.title("Hotel Management System")   # corrected title
        self.root.geometry("1550x800+0+0")

        # helper to load images safely (returns PhotoImage)
        def load_image(path, size):
            try:
                img = Image.open(path)
                img = img.resize(size, Image.LANCZOS)
            except Exception:
                # create a plain placeholder image so program doesn't crash
                img = Image.new("RGB", size, (200, 200, 200))
            return ImageTk.PhotoImage(img)

        # ==================1st img===================
        img1_path = r"C:\Users\HP\OneDrive\Desktop\Hotel Management System\hotel images\hotel1.png"
        self.photoimg1 = load_image(img1_path, (1550, 140))

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # =================logo=======================
        img2_path = r"C:\Users\HP\OneDrive\Desktop\Hotel Management System\hotel images\logohotel.png"
        self.photoimg2 = load_image(img2_path, (230, 140))

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

        # ====================title===============
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM",
                          font=("times new roman", 40, "bold"),
                          bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # ===============main frame=================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # ============= menu=======================
        lbl_menu = Label(main_frame, text="MENU",
                         font=("times new roman", 20, "bold"),
                         bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # =============buttons frame===========
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_details,
                          width=22, font=("times new roman", 14, "bold"),
                          bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="ROOM", command=self.open_room_booking, width=22,
                          font=("times new roman", 14, "bold"),
                          bg="black", fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS", width=22,
                             font=("times new roman", 14, "bold"),
                             bg="black", fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT", width=22,
                            font=("times new roman", 14, "bold"),
                            bg="black", fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=22,
                            font=("times new roman", 14, "bold"),
                            bg="black", fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=1)

        # ================right side image================
        img3_path = r"C:\Users\HP\OneDrive\Desktop\Hotel Management System\hotel images\slide3.jpg"
        self.photoimg3 = load_image(img3_path, (1310, 590))

        lblimg = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg.place(x=225, y=0, width=1310, height=590)

        # =============down image============
        img4_path = r"C:\Users\HP\OneDrive\Desktop\Hotel Management System\hotel images\myh.jpg"
        self.photoimg4 = load_image(img4_path, (230, 210))

        lblimg = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=225, width=230, height=210)

        img5_path = r"C:\Users\HP\OneDrive\Desktop\Hotel Management System\hotel images\khana.jpg"
        self.photoimg5 = load_image(img5_path, (230, 190))

        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=420, width=230, height=190)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def open_room_booking(self):
        """
        Attempt to open a RoomBooking window class from common module names.
        If not found, open a placeholder Toplevel so app doesn't crash.
        """
        # list of likely module names where RoomBooking class might live
        candidates = ["room", "room_booking", "room_book", "roombooking", "room_booking_system"]
        RoomClass = None

        for mod_name in candidates:
            try:
                mod = importlib.import_module(mod_name)
                if hasattr(mod, "RoomBooking"):
                    RoomClass = getattr(mod, "RoomBooking")
                    break
            except Exception:
                # ignore import errors, keep trying other candidates
                pass

        # If not found in external modules, check globals (in case user defined it in same file)
        if RoomClass is None and "RoomBooking" in globals() and isinstance(globals()["RoomBooking"], type):
            RoomClass = globals()["RoomBooking"]

        if RoomClass:
            try:
                self.new_window = Toplevel(self.root)
                self.app = RoomClass(self.new_window)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open RoomBooking window:\n{e}")
        else:
            # fallback placeholder window (does not change your main UI)
            self.new_window = Toplevel(self.root)
            self.new_window.title("Room Booking")
            self.new_window.geometry("600x400+200+200")
            Label(
                self.new_window,
                text="Room Booking window not found.\n"
                     "If you have an external RoomBooking class, name its file\n"
                     "room.py or room_booking.py (module will be auto-detected).",
                font=("times new roman", 14)
            ).pack(padx=20, pady=40)
            Button(
                self.new_window,
                text="Close",
                command=self.new_window.destroy,
                font=("times new roman", 12)
            ).pack(pady=10)


if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
