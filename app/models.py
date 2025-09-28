"""Database models for the Flask application."""
from flask_login import UserMixin
from . import db, login_manager


class User(UserMixin, db.Model):
    """User account model."""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self) -> str:
        return f"<User {self.email}>"


@login_manager.user_loader
def load_user(user_id: str):
    """Load a user for Flask-Login from the database."""
    return User.query.get(int(user_id))
