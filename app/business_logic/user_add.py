from app import db
from app.database.user_table import UserModel


def add_user(username,
             password):
    db.session.add(UserModel(username=username,
                             password=password))
    db.session.commit()
    return True
