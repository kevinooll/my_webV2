from flask import Blueprint, render_template
import os
from flask import render_template, url_for,current_app
import json
bp = Blueprint("main", __name__)

@bp.get("/")
def home():
    return render_template("home.html")

@bp.get("/pricing")
def pricing():
    return render_template("pricing.html")

@bp.get("/teachers")
def teachers():
    return render_template("teachers.html")

@bp.get("/faq")
def faq():
    return render_template("faq.html")

@bp.get("/contact")
def contact():
    return render_template("contact.html")
@bp.route("/courses/speaking")
def speaking_course():
    return render_template("speaking_course.html")
@bp.route("/instagram")
def instagram():
    json_path = os.path.join(current_app.root_path, "data", "ig_posts.json")

    with open(json_path, "r", encoding="utf-8") as f:
        posts = json.load(f)

    categories = [
        {
            "id": "featured",
            "name": "精選作品",
            "icon": "⭐",
            "desc": "JenTalk English 最具代表性的學習內容與品牌作品。"
        },
        {
            "id": "speaking",
            "name": "Speaking",
            "icon": "🎤",
            "desc": "練習日常開口、回答問題與自然表達。"
        },
        {
            "id": "listening",
            "name": "Listening",
            "icon": "🎧",
            "desc": "短篇聽力、生活對話與聽力測驗。"
        },
        {
            "id": "travel",
            "name": "生活旅遊",
            "icon": "🌍",
            "desc": "餐廳、機場、咖啡廳、旅遊情境英文。"
        },
        {
            "id": "reviews",
            "name": "學員回饋",
            "icon": "💬",
            "desc": "真實學員心得、上課感受與進步紀錄。"
        },
        {
            "id": "news",
            "name": "新聞news",
            "icon": "📰",
            "desc": "新聞時事，英文學以致用。"
        }
    ]

    return render_template("instagram.html", posts=posts, categories=categories)