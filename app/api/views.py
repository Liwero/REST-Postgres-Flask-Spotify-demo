from flask import Blueprint


spotify_blueprint = Blueprint("demo",
                              __name__)


@spotify_blueprint.route('/', methods=["GET"])
def ping():
    return "Hello this is only demo version :) "


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