from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from src.application.models import models  # noqa
from src.application.urls import url_pattern
from src.infra.environments.variables import DATABASE_URL


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)

    register_extensions(app)
    register_urls(app)
    return app


def register_extensions(app):
    from src.application.extensions import db

    db.init_app(app)
    Migrate(app, db)


def register_urls(app):
    for url_path in url_pattern:
        app.add_url_rule(url_path.path, view_func=url_path.view_func)
