"""Route definitions for the Flask application."""
from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user

from . import bcrypt, db
from .forms import LoginForm, SignUpForm
from .models import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/")
@login_required
def home():
    """Home page displayed after successful login."""
    return render_template("home.html", email=current_user.email)


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    """Handle new user registration."""
    if current_user.is_authenticated:
        return redirect(url_for("auth.home"))

    form = SignUpForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data.lower()).first()
        if existing_user:
            flash("An account with that email already exists.", "warning")
            return redirect(url_for("auth.signup"))

        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        new_user = User(email=form.email.data.lower(), password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully. Please log in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("signup.html", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """Authenticate an existing user."""
    if current_user.is_authenticated:
        return redirect(url_for("auth.home"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash("Logged in successfully.", "success")
            return redirect(url_for("auth.home"))
        flash("Invalid email or password.", "danger")

    return render_template("login.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    """Log out the current user."""
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))
