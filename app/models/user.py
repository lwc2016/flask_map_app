# encoding: utf-8
from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    """用户数据模型"""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    _password = db.Column(db.String(100), nullable=False)
    createdTime = db.Column(db.DateTime, default=datetime.now)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    # 判断密码是否正确
    def password_validate(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User {name}>".format(name=self.name)

@login_manager.user_loader
def user_loader(userId):
    print("userId:", userId)
    return User.query.filter_by(id=userId).first()