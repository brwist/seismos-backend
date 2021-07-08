import os

from flask import Flask
from flask_restful import Api
from app.views import ENDPOINTS_MAP
from flask_sqlalchemy import SQLAlchemy

# instantiate extensions
db = SQLAlchemy()


def create_app(environment="development"):
    from config import config
    # from app.models import (
    #     User,
    #     AnonymousUser,
    # )

    # Instantiate app.
    app = Flask(__name__)
    api = Api(app)

    for resource, url in ENDPOINTS_MAP.items():
        api.add_resource(resource, url)

    # Set app config.
    env = os.environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])
    config[env].configure(app)
    db.init_app(app)

    # Set up extensions.
    # login_manager.init_app(app)
    
    # Set up flask login.
    # @login_manager.user_loader
    # def get_user(id):
    #     return User.query.get(int(id))

    # login_manager.login_view = "auth.login"
    # login_manager.login_message_category = "info"
    # login_manager.anonymous_user = AnonymousUser

    # # Error handlers.
    # @app.errorhandler(HTTPException)
    # def handle_http_error(exc):
    #     return render_template("error.html", error=exc), exc.code

    return app
