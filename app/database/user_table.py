from passlib.apps import custom_app_context as hash_method

from app import db


class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String())
    password_hash = db.Column(db.String())
    login_status = db.Column(db.Boolean(),
                             nullable=True)
    login_time = db.Column(db.DateTime,
                           nullable=True)
    token = db.Column(db.String(),
                      nullable=True)

    def __init__(self,
                 username,
                 password,
                 login_status=False,
                 login_time=None,
                 token=""):
        self.username = username
        self.password_hash = hash_method.encrypt(password)
        self.login_status = login_status
        self.login_time = login_time
        self.token = token


def verify_password(password_hash, password):
    return hash_method.verify(password, password_hash)
