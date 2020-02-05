import logging

from app import db
from app.database.user_table import UserModel


from app.tools.method_response import MethodResponse


def add_user(username: str,
             password: str) -> MethodResponse:
    """
    Method responsible to add user in db
    :param username: username pass in payload
    :param password: password pass in payload
    :return: Method Response structure
    """
    try:
        logging.info(msg="Checking provided credentials")
        if username or password is None:
            logging.error(msg="No username or password")
            return MethodResponse(message="Username or Password not provided")
        logging.info(msg="Finding user in db")
        db.session.add(UserModel(username=username,
                                 password=password))
        db.session.commit()
        return MethodResponse(success=True,
                              message="Usern has been addedd to the database. Now you can sign in")
    except Exception as e:
        logging.error(msg="problem occured {}".format(e))
        db.session.rollback()
        return MethodResponse(message="Problem occured",
                              data=format(e))


def find_user_by_username(username: str,
                          password: str=None
                          ) -> MethodResponse:
    """
    Method responsible for finding user in db or if password is not None finding username in db

    To think, we can manage by one method to find username, find out if username is unique, blocking possibility of adding users with ssame username

    :param username: username
    :param password: password only to verify if password is correct
    :return: Method Response structure
    """
    if username is None:
        return MethodResponse(message="Username not provided")
    if password is None:
        if count_users(username) == 0:

            user = db.session.query(UserModel).filter(UserModel.username == username).all()
        elif count_users(username) == 1:
            pass
        else:
            pass
    pass


def log_in() -> MethodResponse:
    pass


def delete_user() -> MethodResponse:
    # for admin only
    pass


def count_users(username) -> int:
    count = db.session.query(UserModel).filter(
        UserModel.mam_id == username).count()
    return count
