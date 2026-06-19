from flask import Flask
from .config import Config
from .extensions import db, login_manager, csrf

def create_app():


    app = Flask(__name__)

    print("STATIC_URL_PATH =", app.static_url_path)
    print("STATIC_FOLDER   =", app.static_folder)
    print("ROOT_PATH       =", app.root_path)


    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    from .main.routes import bp as main_bp
    from .auth.routes import bp as auth_bp
    from .booking.routes import bp as booking_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(booking_bp, url_prefix="/booking")

    with app.app_context():
        db.create_all()

    return app
