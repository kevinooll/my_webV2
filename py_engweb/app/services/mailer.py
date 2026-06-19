import os
import smtplib
from email.mime.text import MIMEText

def send_booking_email(booking):
    host = os.getenv("SMTP_HOST")
    user = os.getenv("SMTP_USER")
    pw = os.getenv("SMTP_PASS")
    mail_from = os.getenv("MAIL_FROM", user)
    if not host or not user or not pw:
        return

    subject = f"[JenTalk] 新試聽預約：{booking.name}"
    body = f"""新試聽預約

姓名：{booking.name}
Email：{booking.email}
LINE：{booking.line_id}
目標：{booking.goal}
程度：{booking.level}
偏好時間：{booking.preferred_time}

備註：
{booking.message}
"""
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = mail_from
    msg["To"] = user  # 管理員收件

    with smtplib.SMTP(host, int(os.getenv("SMTP_PORT","587"))) as s:
        s.starttls()
        s.login(user, pw)
        s.sendmail(user, [user], msg.as_string())
