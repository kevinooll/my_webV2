import os
from datetime import datetime, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build

def try_create_calendar_event(booking):
    sa_path = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")
    cal_id = os.getenv("GOOGLE_CALENDAR_ID")
    if not sa_path or not cal_id or not os.path.exists(sa_path):
        return None

    creds = service_account.Credentials.from_service_account_file(
        sa_path,
        scopes=["https://www.googleapis.com/auth/calendar"]
    )
    service = build("calendar", "v3", credentials=creds)

    # 這裡示範：你可以把 preferred_time 先當文字存，真正上線建議改成 datetime 欄位
    start = datetime.utcnow() + timedelta(days=1)
    end = start + timedelta(minutes=30)

    event = {
        "summary": f"JenTalk 試聽｜{booking.name}",
        "description": f"Goal: {booking.goal}\nLevel: {booking.level}\nEmail: {booking.email}\nLINE: {booking.line_id}\nMsg: {booking.message}",
        "start": {"dateTime": start.isoformat() + "Z"},
        "end": {"dateTime": end.isoformat() + "Z"},
    }

    created = service.events().insert(calendarId=cal_id, body=event).execute()
    return created.get("id")
