from flask import Blueprint
import logging

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
     <h2>If you are looking an album of your favourite singer (/search/album)</h2>
     <h2>If you want to get random song (/random_song)</h2>
     </body>
     </html>"""


@spotify_blueprint.route('/registry', methods=["POST"])
def registry():
    pass


@spotify_blueprint.route('/login', methods=["POST"])
def login():
    pass


@spotify_blueprint.route('/search/album', methods=['POST'])
def search_album():
    pass


@spotify_blueprint.route('/random_song', methods=["GET"])
def get_random_song():
    pass
