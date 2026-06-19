from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user
from ..extensions import db
from ..models import User

bp = Blueprint("auth", __name__)

@bp.get("/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    return render_template("auth_login.html")

@bp.post("/login")
def login_post():
    email = request.form.get("email","").strip().lower()
    password = request.form.get("password","")
    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        flash("帳號或密碼錯誤", "error")
        return redirect(url_for("auth.login"))
    login_user(user)
    return redirect(url_for("main.home"))

@bp.get("/register")
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    return render_template("auth_register.html")

@bp.post("/register")
def register_post():
    email = request.form.get("email","").strip().lower()
    password = request.form.get("password","")
    if not email or not password:
        flash("請輸入 Email 與密碼", "error")
        return redirect(url_for("auth.register"))
    if User.query.filter_by(email=email).first():
        flash("Email 已註冊", "error")
        return redirect(url_for("auth.register"))
    u = User(email=email)
    u.set_password(password)
    db.session.add(u)
    db.session.commit()
    flash("註冊成功，請登入", "success")
    return redirect(url_for("auth.login"))

@bp.get("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))
