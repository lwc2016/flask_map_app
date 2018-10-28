# encoding: utf-8
from app import db
from datetime import datetime

class Location(db.Model):
    """省数据模型"""
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(8), unique=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    provinceCode = db.Column(db.String(8), nullable=True)
    cityCode = db.Column(db.String(8), nullable=True)
    createdTime = db.Column(db.DateTime, default=datetime.now)

    #shops = db.relationship("Shop", backref="locations")
    def toJson(self):
        return {
            "code": self.code,
            "name": self.name
        }

