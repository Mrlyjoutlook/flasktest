# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from blog.controllers.home import Home

app = Flask(__name__)
api = Api(app)

api.add_resource(Home, '/')