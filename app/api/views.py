from flask import Blueprint, request
import logging

from app.business_logic.user_bl import add_user, log_in
from app.tools.method_response import MethodResponse
from app.tools.validate_flask_req import validate_post_req

spotify_blueprint = Blueprint("demo",
                              __name__)


@spotify_blueprint.route('/', methods=["GET"])
def ping():
    logging.info(msg="Sending messages to welcome new user")
    return """<html>
    <head></head>
    <body>
    <h1>Hello this is only demo version :) </h1>
     <h2>You can easily create your account by sending your username and password (endpoint /registry)</h2>
     <h2>After that you need to sign in to have access to demo app (endpoint /login)</h2>
     <h2>[NOT READY] If you are looking an album of your favourite singer (/search/album)</h2>
     <h2>If you want to get random song (/random_song)</h2>
     </body>
     </html>"""


@spotify_blueprint.route('/registry', methods=["POST"])
def registry():
    param_list = ["username", "password"]
    result = validate_post_req(request,
                               params_list=param_list)
    if not result.success:
        return MethodResponse.return_error(message=result.message)
    username = result.data[0]
    password = result.data[1]
    if add_user(username=username,
                password=password).success:
        return MethodResponse.return_success(message="You have been register in demo app."
                                                     " Now you can login")
    else:
        return MethodResponse.return_error(message="Something goes wrong please try again")


@spotify_blueprint.route('/login', methods=["POST"])
def login():
    param_list = ["username", "password"]
    result = validate_post_req(request,
                               params_list=param_list)
    if not result.success:
        return MethodResponse.return_error(message=result.message)
    username = result.data[0]
    password = result.data[1]
    tokens = log_in(username=username,
                    password=password)
    if tokens.success:
        return MethodResponse.return_success(message="Sucessfully login to demo app Token in data section",
                                             data=tokens.data)
    else:
        return MethodResponse.return_error(message="Cannot login, please try again")


@spotify_blueprint.route('/random_song', methods=["GET"])
def get_random_song():
    pass


# @spotify_blueprint.route('/search/album', methods=['POST'])
# def search_album():
#     pass
