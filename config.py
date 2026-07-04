import os
from dotenv import load_dotenv

load_dotenv()

# ==========================
# WhatsApp Cloud API
# ==========================

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

ADMIN_PHONE = os.getenv("ADMIN_PHONE")


# ==========================
# Database
# ==========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_DIR = os.path.join(BASE_DIR, "database")

# Create database folder automatically if it doesn't exist
os.makedirs(DB_DIR, exist_ok=True)

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{os.path.join(DB_DIR, 'janaseva.db')}"
)