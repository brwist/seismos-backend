import pytest

from app import db, create_app


@pytest.fixture
def client():
    app = create_app(environment="testing")

    with app.test_client() as client:
        app_ctx = app.app_context()
        app_ctx.push()
        db.drop_all()
        db.create_all()
        yield client
        db.session.remove()
        db.drop_all()
        app_ctx.pop()


def test_db_create_user(client):
    from app.models import User
    username, passwd = "imgroot", "1234"
    user = User(username=username, password=passwd, email="imgroot@gmail.com")
    user.save()

    user = User.query.filter(User.username == username).first()
    assert user
    assert user.username == username
