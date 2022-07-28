from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from src.main.environments.variables import DATABASE_URL
from src.main.routes.client_routes import api_routes_bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    CORS(app)

    app.register_blueprint(api_routes_bp)
    register_extensions(app)
    return app


def register_extensions(app):
    from src.main.config.extensions import db

    db.init_app(app)
    migrate = Migrate(app, db)
