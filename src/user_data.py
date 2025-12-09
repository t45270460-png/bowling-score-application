from src.user import User
import os
from dotenv import load_dotenv

load_dotenv()
USERS = [
    User("testuser1", "password123"),
    User("testuser2", "password234"),
]

ADMIN = User(os.getenv("ADMIN_ID"), os.getenv("ADMIN_PASSWORD"), is_admin=True)
