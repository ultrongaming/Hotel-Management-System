import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "hotel images")

# Database
DB_PATH = os.path.join(BASE_DIR, "hotel.db")

# Common image paths
LOGO_PATH = os.path.join(IMAGES_DIR, "logohotel.png")
HOTEL_BG_PATH = os.path.join(IMAGES_DIR, "hotel1.png")
SLIDE_PATH = os.path.join(IMAGES_DIR, "slide3.jpg")
BED_PATH = os.path.join(IMAGES_DIR, "bed.jpg")
FOOD_PATH = os.path.join(IMAGES_DIR, "khana.jpg")
MYH_PATH = os.path.join(IMAGES_DIR, "myh.jpg")
