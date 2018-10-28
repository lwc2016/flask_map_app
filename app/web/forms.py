# encoding: utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    name = StringField("name", validators=[DataRequired(message="请填写账户！")])
    password = PasswordField("password", validators=[DataRequired(message="请填写密码！")])

class AddShopForm(FlaskForm):
    name = StringField("name", validators=[DataRequired(message="请填写门店名称")])
    province = StringField("provinceCode", validators=[DataRequired("请选择省！")])
    city = StringField("cityCode", validators=[DataRequired("请选择市！")])
    area = StringField("areaCode", validators=[DataRequired("请选择区！")])
    address = StringField("address", validators=[DataRequired("请填写详细地址")])
    longitude = StringField("longitude")
    latitude = StringField("latitude")