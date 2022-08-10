from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from src.main.environments.variables import DATABASE_URL
from src.main.routes.auth_routes import AuthenticateClientRoute
from src.infra.config.registered_models import models  # noqa
from src.main.routes.urls import url_pattern


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)

    register_extensions(app)
    register_urls(app)
    return app


def register_extensions(app):
    from src.main.config.extensions import db

    db.init_app(app)
    Migrate(app, db)


def register_urls(app):
    for url_path in url_pattern:
        app.add_url_rule(url_path.path, view_func=url_path.view_func)
