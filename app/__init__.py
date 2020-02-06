import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.tools.prepare_env import load_dot_env

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask('spotify_demo')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".\
        format(os.environ.get("DB_USER",),
               os.environ.get("DB_PASSWORD"),
               os.environ.get("DB_HOST"),
               os.environ.get("DB_PORT"),
               os.environ.get("DB_NAME"))
    load_dot_env()
    configure_extensions(app)
    register_blueprint(app)
    return app


def register_blueprint(app: Flask):
    from app import api
    app.register_blueprint(api.views.spotify_blueprint)


def configure_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app,
                     db)
