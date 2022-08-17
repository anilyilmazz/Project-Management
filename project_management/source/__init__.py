from flask.app import Flask
from .config import config_by_name
from mongoengine import connect


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    connect(host=app.config["MONGODB_URI"])
    return app
