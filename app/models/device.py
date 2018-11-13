# encoding: utf-8
from app import db

class Device(db.Model):
    __tablename__ = "devices"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sn = db.Column(db.String(32), nullable=False)
    google_lng = db.Column(db.Numeric(18, 15), nullable=False)
    google_lat = db.Column(db.Numeric(18, 15), nullable=False)
    baidu_lng = db.Column(db.Numeric(18, 15), nullable=False)
    baidu_lat = db.Column(db.Numeric(18, 15), nullable=False)

    def toJson(self):
        return {
            "id": self.id,
            "sn": self.sn,
            "google_lng": float(self.google_lng) ,
            "google_lat": float(self.google_lat),
            "baidu_lng": float(self.baidu_lng),
            "baidu_lat": float(self.baidu_lat)
        }