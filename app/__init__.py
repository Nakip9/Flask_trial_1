from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf import CSRFProtect

# Initialize extensions
bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()


def create_app():
    """Application factory for the Flask app."""
    app = Flask(__name__)

    # Basic configuration
    app.config["SECRET_KEY"] = "change-me"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions with the app
    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"

    # Register blueprints
    from .routes import auth_bp

    app.register_blueprint(auth_bp)

    # Create the database tables when the app starts
    with app.app_context():
        db.create_all()

    return app
