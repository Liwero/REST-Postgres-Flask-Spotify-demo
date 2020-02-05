import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask('spotify_demo')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_CONNECTION")
    db.init_app(app)
    migrate.init_app(app, db)
    register_blueprint(app)
    return app


def register_blueprint(app: Flask):
    from app import api
    app.register_blueprint(api.views.spotify_blueprint)