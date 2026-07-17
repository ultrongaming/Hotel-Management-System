import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from customer import Cust_Win
import importlib
from config import IMAGES_DIR, LOGO_PATH, HOTEL_BG_PATH, SLIDE_PATH, MYH_PATH, FOOD_PATH

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("EliteStay Hotel Management System")
        self.root.geometry("1550x800+0+0")
        self.root.configure(bg="#f0f0f0")

        # Style configuration for professional look
        style = ttk.Style()
        style.theme_use("clam")  # Modern theme

        self.load_images()
        self.create_ui()

    def load_images(self):
        """Load all images with error handling and relative paths."""
        def safe_load_image(path, size):
            try:
                img = Image.open(path)
                img = img.resize(size, Image.LANCZOS)
                return ImageTk.PhotoImage(img)
            except Exception:
                # Placeholder
                placeholder = Image.new("RGB", size, (100, 100, 100))
                return ImageTk.PhotoImage(placeholder)

        self.photoimg1 = safe_load_image(HOTEL_BG_PATH, (1550, 140))
        self.photoimg2 = safe_load_image(LOGO_PATH, (230, 140))
        self.photoimg3 = safe_load_image(SLIDE_PATH, (1310, 590))
        self.photoimg4 = safe_load_image(MYH_PATH, (230, 210))
        self.photoimg5 = safe_load_image(FOOD_PATH, (230, 190))

    def create_ui(self):
        """Create the main UI components."""
        # Top banner
        lblimg1 = tk.Label(self.root, image=self.photoimg1, bd=4, relief=tk.RIDGE)
        lblimg1.place(x=0, y=0, width=1550, height=140)

        # Logo
        lblimg2 = tk.Label(self.root, image=self.photoimg2, bd=4, relief=tk.RIDGE)
        lblimg2.place(x=0, y=0, width=230, height=140)

        # Title
        lbl_title = tk.Label(
            self.root,
            text="ELITESTAY HOTEL MANAGEMENT SYSTEM",
            font=("Helvetica", 40, "bold"),
            bg="black",
            fg="#ffd700",  # Gold
            bd=4,
            relief=tk.RIDGE
        )
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # Main frame
        main_frame = tk.Frame(self.root, bd=4, relief=tk.RIDGE, bg="#f0f0f0")
        main_frame.place(x=0, y=190, width=1550, height=610)

        # Menu sidebar
        self.create_menu(main_frame)

        # Right side image
        lblimg3 = tk.Label(main_frame, image=self.photoimg3, bd=4, relief=tk.RIDGE)
        lblimg3.place(x=230, y=0, width=1310, height=590)

        # Bottom images
        lblimg4 = tk.Label(main_frame, image=self.photoimg4, bd=4, relief=tk.RIDGE)
        lblimg4.place(x=0, y=225, width=230, height=210)

        lblimg5 = tk.Label(main_frame, image=self.photoimg5, bd=4, relief=tk.RIDGE)
        lblimg5.place(x=0, y=435, width=230, height=175)

    def create_menu(self, parent):
        """Create professional menu sidebar."""
        # Menu label
        lbl_menu = tk.Label(
            parent,
            text="MAIN MENU",
            font=("Helvetica", 20, "bold"),
            bg="#333333",
            fg="#ffd700",
            bd=4,
            relief=tk.RIDGE
        )
        lbl_menu.place(x=0, y=0, width=230, height=40)

        # Buttons frame
        btn_frame = tk.Frame(parent, bd=4, relief=tk.RIDGE, bg="#333333")
        btn_frame.place(x=0, y=40, width=230, height=250)

        # Button style
        btn_style = {
            "font": ("Helvetica", 14, "bold"),
            "bg": "#1a1a1a",
            "fg": "#ffd700",
            "bd": 0,
            "activebackground": "#ffd700",
            "activeforeground": "black",
            "cursor": "hand2",
            "width": 22,
            "height": 2
        }

        tk.Button(btn_frame, text="CUSTOMER DETAILS", command=self.cust_details, **btn_style).grid(row=0, column=0, pady=5, padx=5)
        tk.Button(btn_frame, text="ROOM BOOKING", command=self.open_room_booking, **btn_style).grid(row=1, column=0, pady=5, padx=5)
        tk.Button(btn_frame, text="ROOM DETAILS", command=self.room_details, **btn_style).grid(row=2, column=0, pady=5, padx=5)
        tk.Button(btn_frame, text="REPORTS", command=self.generate_reports, **btn_style).grid(row=3, column=0, pady=5, padx=5)
        tk.Button(btn_frame, text="LOGOUT", command=self.logout, **btn_style).grid(row=4, column=0, pady=5, padx=5)

    def cust_details(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Customer Management")
        self.app = Cust_Win(self.new_window)

    def open_room_booking(self):
        try:
            from room import RoomBooking
            self.new_window = tk.Toplevel(self.root)
            self.new_window.title("Room Booking")
            self.app = RoomBooking(self.new_window)
        except ImportError as e:
            messagebox.showerror("Error", f"Room module not found: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open room booking: {e}")

    def room_details(self):
        messagebox.showinfo("Coming Soon", "Room details module under development.")

    def generate_reports(self):
        messagebox.showinfo("Reports", "Advanced reporting features coming soon.")

    def logout(self):
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementSystem(root)
    root.mainloop()
