import pytest
from app import create_app, db
from .utils import USER_CREDS
from app.models import User


@pytest.fixture(scope="session")
def client_with_user():
    app = create_app(environment="testing")

    with app.test_client() as client:
        app_ctx = app.app_context()
        app_ctx.push()
        db.session.begin_nested()
        db.drop_all()
        db.create_all()
        user = User(
            username=USER_CREDS["username"],
            password=USER_CREDS["password"],
            email=f"{USER_CREDS['username']}@gmail.com"
        )
        user.save()
        yield client
        # clear test
        user.delete()
        db.session.remove()
        db.drop_all()
        db.session.rollback()
        app_ctx.pop()
