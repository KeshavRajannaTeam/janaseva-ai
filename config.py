import os
from dotenv import load_dotenv

load_dotenv()

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

ADMIN_PHONE = os.getenv("ADMIN_PHONE")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///database/janaseva.db"
)