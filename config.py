# encoding: utf-8

# 环境配置
ENV = "development"
DEBUG = True

# secret_key
SECRET_KEY = "123456"

# mysql配置
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost:3306/maps"
SQLALCHEMY_TRACK_MODIFICATIONS = True