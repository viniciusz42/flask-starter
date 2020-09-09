import os
import sys
from flask import Flask, Blueprint
from flask_restplus import Api
from dotenv import load_dotenv, find_dotenv
from .core.config import CONFIG_ENV
from .freelancers.resources import ns as challenge

api = Api(title="Desafio Órama")
app = Flask(__name__)
load_dotenv(find_dotenv())


def validate():
    env = os.getenv("FLASK_CONFIG")
    if env is None or env not in CONFIG_ENV:
        app.logger.error("Env não encontrado ou inválido")
        sys.exit(1)


def start_server():
    validate()
    app.config.from_object(CONFIG_ENV[os.getenv("FLASK_CONFIG")])
    blueprint = Blueprint("api", __name__)
    api.init_app(blueprint)
    api.add_namespace(challenge, path="/")
    app.register_blueprint(blueprint)
    return app

