from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..extensions import db
from ..models import TrialBooking
from ..services.google_calendar import try_create_calendar_event
from ..services.mailer import send_booking_email
from ..services.notifier import notify_admin

bp = Blueprint("booking", __name__)

@bp.route("/trial", methods=["GET"])
def trial_booking():
    return render_template("booking_trial.html")
@bp.get("/trial")
def trial_form():
    return render_template("booking_trial.html")

@bp.post("/trial")
def trial_submit():
    data = {
        "name": request.form.get("name","").strip(),
        "email": request.form.get("email","").strip(),
        "line_id": request.form.get("line_id","").strip(),
        "goal": request.form.get("goal","").strip(),
        "level": request.form.get("level","").strip(),
        "preferred_time": request.form.get("preferred_time","").strip(),
        "message": request.form.get("message","").strip(),
    }
    if not data["name"] or not data["email"] or not data["goal"] or not data["level"] or not data["preferred_time"]:
        flash("請填寫必填欄位", "error")
        return redirect(url_for("booking.trial_form"))

    b = TrialBooking(**data)
    db.session.add(b)
    db.session.commit()

    # 1) Google Calendar（可選）
    event_id = try_create_calendar_event(b)
    if event_id:
        b.calendar_event_id = event_id
        b.status = "calendar_added"
        db.session.commit()

    # 2) Email（可選）
    send_booking_email(b)

    # 3) 通知（可選：Telegram or LINE OA）
    notify_admin(b)

    b.status = "notified"
    db.session.commit()

    return render_template("booking_success.html", booking=b)
