from flask_login import UserMixin
from dotenv import load_dotenv

load_dotenv()


class User(UserMixin):
    def __init__(self, init_id, password, is_admin=False):
        self.id = init_id
        self.password = password
        self.is_admin = is_admin
