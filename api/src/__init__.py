# from flask_restplus import Resource, Api
from flask import Flask
from src.routes import routes


def create_app(config_name):
    
    app = Flask(__name__)
    # app.config.from_object(config[config_name])
    routes.init_app(app)
    return app
