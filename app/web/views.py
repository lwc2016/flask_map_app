# encoding: utf-8
from app import db
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, login_user, logout_user
from .forms import LoginForm, AddShopForm
from app.models.user import User
from app.models.shop import Shop
from app.models.device import Device
from app.models.location import Location
from . import blueprint
from ..utils import map


@blueprint.route("/")
@login_required
def index():
    shops = Shop.query.limit(8).all()
    return render_template("index_baidu.html", shops=shops)

@blueprint.route("/google")
@login_required
def google():
    shops = Shop.query.limit(8).all()
    return render_template("index_google.html", shops=shops)

@blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "GET":
        return render_template("login.html", form=form)
    else:
        if form.validate_on_submit():
            user = User.query.filter_by(name=form.name.data).first()
            if user and user.password_validate(form.password.data):
                login_user(user)
                return redirect(url_for("web.index"))
            else:
                flash({"error": ["用户名或密码错误！"]})
                return render_template("login.html", form=form)
        else:
            flash(form.errors)
            return render_template("login.html", form=form)


@blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("web.login"))


@blueprint.route("/shop/add", methods=["GET", "POST"])
def shop_add():
    provinces = Location.query.filter_by(provinceCode=None).all()
    if request.method == "GET":
        return render_template("shop_save.html", provinces=provinces)
    else:
        form = AddShopForm()
        if form.validate_on_submit():
            # 判断门店是否存在
            resp = map.googleToBaidu(form.data["longitude"], form.data["latitude"])

            baidu_lng = resp["result"][0].get("x")
            baidu_lat = resp["result"][0].get("y")

            if Shop.name_existed(form.data.get("name")):
                flash({"name": ["门店已存在！"]})
                return render_template("shop_save.html", provinces=provinces)
            shop = Shop(name=form.data["name"],
                        province=form.data["province"],
                        city=form.data["city"],
                        area=form.data["area"],
                        address=form.data["address"],
                        google_lng=form.data["longitude"],
                        google_lat=form.data["latitude"],
                        baidu_lng=baidu_lng,
                        baidu_lat=baidu_lat
                        )
            db.session.add(shop)
            db.session.commit()
            return redirect(url_for("web.index"))
        else:
            flash(form.errors)
            return render_template("shop_save.html", provinces=provinces)


@blueprint.route("/shop/delete/<int:id>", methods=["GET"])
def shop_delete(id):
    shop = Shop.query.filter_by(id=id).first()
    db.session.delete(shop)
    db.session.commit()
    return redirect(url_for("web.index"))

@blueprint.route("/device/google", methods=["GET"])
def device_google():
    devices = Device.query.all()
    return render_template("device_google.html", devices=devices)

@blueprint.route("/device/baidu", methods=["GET"])
def device_baidu():
    devices = Device.query.all()
    return render_template("device_baidu.html", devices=devices)
