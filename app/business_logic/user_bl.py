import datetime
import logging
import secrets

from app import db
from sqlalchemy import update
from app.database.user_table import UserModel, verify_password

from app.tools.method_response import MethodResponse


def add_user(username: str,
             password: str) -> MethodResponse:
    """
    Method responsible to add user in db
    :param username: username pass in payload
    :param password: password pass in payload
    :return: Method Response structure
    """
    logging.info(msg="Checking provided credentials")
    if not username or not password:
        logging.error(msg="No username or password")
        return MethodResponse(message="Username or Password not provided")
    logging.info(msg="Finding user in db")
    if find_user_by_username(username=username).success:
        try:
            db.session.add(UserModel(username=username,
                                     password=password))
            db.session.commit()
            logging.info(msg="New user has been added to database Username: {}".format(username))
            return MethodResponse(success=True,
                                  message="You have been register in demo app")
        except Exception as e:
            logging.error(msg="[Adding user] Error with database. {}".format(e))
            return MethodResponse(message="[Adding user] Problem occurred",
                                  data=format(e))
    else:
        return MethodResponse(message="Provide different credentials")


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
            return MethodResponse(success=True,
                                  message="User and Password are unique, can create an account")
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
        if verify_password(password_hash=user.data[0].password_hash,
                           password=password):
            logging.info(msg="Password has been verified")
            user_token = generate_token()
            user_dict = {
                "login_status": True,
                "login_time": datetime.datetime.now(),
                "token": user_token
            }
            if update_user(username,
                        user_dict).success:
                logging.info(msg="User successfully login")
                return MethodResponse(success=True,
                                      message="User successfully login. Please use this token to verify on db",
                                      data=user_token)
            else:
                return MethodResponse(message="Problem with updated record in database")
        else:
            logging.error(msg="Error during logging")
            return MethodResponse(message="Cannot login to account please check credentials")

    else:
        logging.error(msg="No user in database with this credentials")
        return MethodResponse(message="Cannot find user with this credential. Try once more")


def update_user(username: str, user_data: dict) -> MethodResponse:
    if not username:
        return MethodResponse(message="Username not provided")
    try:
        db.session.query(UserModel).filter(UserModel.username == username)\
            .update({UserModel.login_status: user_data.get("login_status"),
                     UserModel.login_time: user_data.get("login_time"),
                     UserModel.token: user_data.get("token")})
        update(UserModel).where(UserModel.username == username).values(login_status=user_data.get("login_status"),
                                                                       login_time=user_data.get("login_time"),
                                                                       token=user_data.get("token"))
        db.session.commit()
        logging.info(msg="User {} has been updated".format(username))
        return MethodResponse(success=True,
                              message="User {} has been updated".format(username))
    except Exception as e:
        logging.error(msg="[Updating User] Problem occured. {}".format(e))
        return MethodResponse(message="[Updating User] Problem occured",
                              data=format(e))


def count_users(username) -> int:
    count = db.session.query(UserModel).filter(
        UserModel.username == username).count()
    return count


def generate_token():
    return secrets.token_urlsafe(20)


def check_time_of_token():
    pass

# def delete_user() -> MethodResponse:
#     # for admin only
#     pass
