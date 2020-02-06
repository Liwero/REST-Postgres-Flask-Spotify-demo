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
                          password: str = None
                          ) -> MethodResponse:
    """
    Method responsible for finding user in db or if password is not None finding username in db

    To think, we can manage by one method to find username, find out if username is unique, blocking possibility of adding users with ssame username

    :param username: username
    :param password: password only to verify if password is correct
    :return: Method Response structure
    """
    if not username:
        return MethodResponse(message="Username not provided")
    if not password:
        if count_users(username) == 0:
            try:
                db.session.add(UserModel(username=username,
                                         password=password)
                               )
                db.session.commit()
                logging.info(msg="New user has been added to database Username: {}".format(username))
                return MethodResponse(success=True,
                                      message="You have been register in demo app")
            except Exception as e:
                logging.error(msg="[Adding user] Error with database. {}".format(e))
                return MethodResponse(message="[Adding user] Problem occurred",
                                      data=format(e))

        else:
            return MethodResponse(message="Please provide different credentials")
    else:
        if count_users(username) == 1:
            try:
                user = db.session.query(UserModel).filter(UserModel.username == username).all()
                logging.info(msg="User has been retrieved")
                return MethodResponse(success=True,
                                      message="User has been successfully retrieved",
                                      data=user)
            except Exception as e:
                logging.error(msg="[Finding user] Problem occurred {}".format(e))
                return MethodResponse(message="[Finding user] Problem occurred",
                                      data=format(e))
        else:
            logging.error(msg="No user with this credentials in database")
            return MethodResponse(message="No user with this credentials in database")


def log_in(username: str,
           password: str) -> MethodResponse:
    """
    Method responsible to log in user and updating record in database with flag and datetime data
    :param username: name of user
    :param password:
    :return:
    """
    if not username or not password:
        return MethodResponse(message="No credentials provided")
    user = find_user_by_username(username=username,
                                 password=password)
    if user.success:
        """update data"""
    else:
        logging.error(msg="No user in database with this credentials")
        return MethodResponse(message="Cannot find user with this credential. Try once more")

    """ Add generation token and sending back to the user, Token will allow to check different endpoints"""


def update_user() -> MethodResponse:
    pass


def delete_user() -> MethodResponse:
    # for admin only
    pass


def count_users(username) -> int:
    count = db.session.query(UserModel).filter(
        UserModel.mam_id == username).count()
    return count
