from flask import Blueprint, render_template

bp = Blueprint("main", __name__)

@bp.route("/")
def home():
    # 先用假資料，之後改成從 DB 撈 Teacher
    teachers = [
        {
            "name": "Alex",
            "tagline": "擅長讓初學者敢開口",
            "skills": ["Travel", "Beginner", "Pronunciation"],
            "avatar": "/static/img/teachers/alex.jpg",
            "slug": "alex"
        },
        {
            "name": "Mia",
            "tagline": "職場英文與面試口說加速",
            "skills": ["Business", "Interview", "Fluency"],
            "avatar": "/static/img/teachers/mia.jpg",
            "slug": "mia"
        },
        {
            "name": "Ryan",
            "tagline": "用情境把句型練到反射",
            "skills": ["Daily", "Grammar in speaking", "Confidence"],
            "avatar": "/static/img/teachers/ryan.jpg",
            "slug": "ryan"
        },
    ]
    return render_template("main/home.html", teachers=teachers)

