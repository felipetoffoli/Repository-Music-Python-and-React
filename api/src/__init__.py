# from flask_restplus import Resource, Api
from flask import Flask
from src.routes import routes
from flask_sqlalchemy import SQLAlchemy
from config import config
# from flask_cors import CORS
db = SQLAlchemy()

def create_app(config_name):
    
    app = Flask(__name__)
    # CORS(app)
    app.config.from_object(config[config_name])
    db.init_app(app)
    routes.init_app(app)
    return app
