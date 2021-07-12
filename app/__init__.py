import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flasgger import Swagger


# instantiate extensions
SWAGGER_TEMPLATE = {"securityDefinitions": {"APIKeyHeader": {"type": "apiKey", "name": "x-access-token", "in": "header"}}}

db = SQLAlchemy()
jwt = JWTManager()
api = Api(prefix="/api")
swagger = Swagger(template=SWAGGER_TEMPLATE)


def create_app(environment="development"):
    from config import config
    from app.views import ENDPOINTS_MAP

    # Instantiate app.
    app = Flask(__name__)
    jwt.init_app(app)
    # Swagger for API DOC
    swagger.init_app(app)

    # Set app config.
    env = os.environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])
    config[env].configure(app)

    for resource, url in ENDPOINTS_MAP.items():
        api.add_resource(resource, url)
    api.init_app(app)
    db.init_app(app)

    return app
