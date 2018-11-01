# encoding: utf-8
from app import db
from datetime import datetime
from .location import Location

class Shop(db.Model):
    """门店数据模型"""
    __tablename__ = "shops"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    province = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    area = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(60), nullable=False)
    google_lng = db.Column(db.Numeric(18, 15), nullable=False)
    google_lat = db.Column(db.Numeric(18, 15), nullable=False)
    baidu_lng = db.Column(db.Numeric(18, 15), nullable=False)
    baidu_lat = db.Column(db.Numeric(18, 15), nullable=False)
    createdTime = db.Column(db.DateTime, default=datetime.now)

    def toJson(self):
        return {
            "id": self.id,
            "name": self.name,
            "province": self.province,
            "city": self.city,
            "area": self.area,
            "address": self.address,
            "google_lng": float(self.google_lng),
            "google_lat": float(self.google_lat),
            "baidu_lng": float(self.baidu_lng),
            "baidu_lat": float(self.baidu_lat)
        }

    @classmethod
    def name_existed(cls, name):
        result = cls.query.filter_by(name=name).first()
        return result
