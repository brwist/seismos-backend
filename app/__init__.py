import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from flask_cors import CORS
from flask_migrate import Migrate

# instantiate extensions
SWAGGER_TEMPLATE = {
    "components": {
        "securitySchemes": {
            "bearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
            }
        }
    }
}

db = SQLAlchemy()
jwt = JWTManager()
api = Api(prefix="/api")
swagger = Swagger(template=SWAGGER_TEMPLATE)


def create_app(environment="development"):
    from config import config
    from app.views import ENDPOINTS_MAP
    from app.models import User

    # Instantiate app.
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)
    # Set app config.
    env = os.environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])
    config[env].configure(app)

    app.config["SWAGGER"] = {
        "title": "Seismos API",
        "uiversion": 3,
        "openapi": "3.0.2",
    }

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.filter_by(id=identity).one_or_none()

    jwt.init_app(app)

    # Swagger for API DOC
    swagger.init_app(app)

    for resource, url in ENDPOINTS_MAP.items():
        api.add_resource(resource, url)

    api.init_app(app)
    db.init_app(app)
    Migrate(app, db)

    return app
