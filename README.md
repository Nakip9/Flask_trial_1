# Flask Trial Authentication App

This project demonstrates a minimal full-stack Flask application with user registration and authentication.

## Features
- User sign-up and login with password hashing via Flask-Bcrypt.
- Session management using Flask-Login with CSRF protection from Flask-WTF.
- SQLite database powered by Flask-SQLAlchemy.
- Simple HTML and CSS interface for registration, login, and a protected home page.

## Getting Started

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python run.py
   ```
   The app will be available at `http://localhost:5000`.

## Project Structure
```
app/
├── __init__.py       # Application factory and extension initialization
├── forms.py          # WTForms form definitions
├── models.py         # Database models
├── routes.py         # Application routes and authentication logic
├── static/
│   └── styles.css    # Basic styling for the pages
└── templates/
    ├── base.html
    ├── home.html
    ├── login.html
    └── signup.html
```

## Database
The application uses SQLite (`app.db`) by default. The database is created automatically on first run.

## Environment Variables
Update `SECRET_KEY` in `app/__init__.py` for production use. You can replace it with an environment variable for improved security.
