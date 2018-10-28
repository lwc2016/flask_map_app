# encoding: utf-8
from flask import request, jsonify
from app import csrf
from . import blueprint
from app.models.location import Location
from app.models.shop import Shop

@blueprint.route("/getCities", methods=["GET", "POST"])
@csrf.exempt
def getCities():
    provinceCode = request.args.get("provinceCode") or request.form.get("provinceCode")
    if not provinceCode:
        return jsonify({"code": "1001", "errorMsg": "缺少必要参数"})
    rows = Location.query.filter_by(provinceCode=provinceCode, cityCode=None).all()
    cities = list(map(lambda item: item.toJson(), rows))
    print(cities)
    return jsonify({"code": "0", "result": cities})

@blueprint.route("/getAreas", methods=["GET", "POST"])
@csrf.exempt
def getAreas():
    cityCode = request.args.get("cityCode") or request.form.get("cityCode")
    if not cityCode:
        return jsonify({"code": "1001", "errorMsg": "缺少必要参数"})
    rows = Location.query.filter_by(cityCode=cityCode).all()
    areas = list(map(lambda item: item.toJson(), rows))
    return jsonify({"code": "0", "result": areas})

@blueprint.route("/shop/list", methods=["GET", "POST"])
@csrf.exempt
def shopList():
    rows = Shop.query.all()
    print(rows)
    shops = list(map(lambda item: item.toJson(), rows))
    return jsonify({"code": 0, "result": shops})