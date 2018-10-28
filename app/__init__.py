# encoding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()
login_manager.login_view = "web.login"

def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    # 初始化
    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)

    # 导入蓝图
    from app.web import blueprint as web
    from app.api import blueprint as api
    # 注册蓝图
    app.register_blueprint(web, url_prefix="/")
    app.register_blueprint(api, url_prefix="/api")
    return app