from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .extensions import db, login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, pw: str):
        self.password_hash = generate_password_hash(pw)

    def check_password(self, pw: str) -> bool:
        return check_password_hash(self.password_hash, pw)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

class TrialBooking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    line_id = db.Column(db.String(80))
    goal = db.Column(db.String(80), nullable=False)
    level = db.Column(db.String(80), nullable=False)
    preferred_time = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    calendar_event_id = db.Column(db.String(255))
    status = db.Column(db.String(30), default="created")  # created / calendar_added / notified
