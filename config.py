# encoding: utf-8
import sys
import os



# 环境配置
ENV = os.environ.get("ENV", "development")
DEBUG = ENV == "development"
PORT = 5000 if ENV == "development" else 8080


# secret_key
SECRET_KEY = "123456"

# mysql配置
if ENV == "development":
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost:3306/maps"
else:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:180625@localhost:3306/maps"

SQLALCHEMY_TRACK_MODIFICATIONS = True