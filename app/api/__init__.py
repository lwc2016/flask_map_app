# encoding: utf-8
from flask import Blueprint
blueprint = Blueprint("api", __name__)

from . import views