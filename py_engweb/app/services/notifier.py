import os
import requests

def notify_admin(booking):
    text = (
        f"📩 新試聽預約\n"
        f"姓名：{booking.name}\n"
        f"Email：{booking.email}\n"
        f"LINE：{booking.line_id}\n"
        f"目標：{booking.goal}\n"
        f"程度：{booking.level}\n"
        f"時間：{booking.preferred_time}\n"
    )

    # 1) Telegram（推薦：最省事）
    tg_token = os.getenv("TELEGRAM_BOT_TOKEN")
    tg_chat = os.getenv("TELEGRAM_CHAT_ID")
    if tg_token and tg_chat:
        url = f"https://api.telegram.org/bot{tg_token}/sendMessage"
        requests.post(url, json={"chat_id": tg_chat, "text": text}, timeout=10)

    # 2) LINE OA Messaging API（可選）
    # 需要 LINE_CHANNEL_ACCESS_TOKEN + LINE_USER_ID（你自己的 line user id）
    line_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    line_user = os.getenv("LINE_USER_ID")
    if line_token and line_user:
        headers = {"Authorization": f"Bearer {line_token}", "Content-Type": "application/json"}
        payload = {
            "to": line_user,
            "messages": [{"type": "text", "text": text}]
        }
        requests.post("https://api.line.me/v2/bot/message/push", headers=headers, json=payload, timeout=10)
