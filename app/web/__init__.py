# encoding: utf-8
from flask import Blueprint

blueprint = Blueprint("web", __name__)

from . import views
