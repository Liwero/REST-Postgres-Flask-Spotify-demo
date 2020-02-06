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

    def __init__(self,
                 username,
                 password):
        self.username = username
        self.password_hash = hash_method.encrypt(password)

    def verify_password(self, password):
        return hash_method.verify(password, self.password_hash)
