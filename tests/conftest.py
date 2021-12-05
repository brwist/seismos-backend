import json
import pytest
from app import create_app, db
from .utils import USER_CREDS, TEST_STATIC_ROOT
from app.models import User, Project


CREATE_PROJECT_JSON_PATH = f"{TEST_STATIC_ROOT}/project_create.json"


def create_client():
    app = create_app(environment="testing")
    with app.test_client() as client:
        app_ctx = app.app_context()
        app_ctx.push()
        return client, app_ctx


def create_test_user():
    user = User(
        username=USER_CREDS["username"],
        password=USER_CREDS["password"],
        email=f"{USER_CREDS['username']}@gmail.com"
    )
    user.save()
    return user


def prepare_user_and_client():
    client, app_ctx = create_client()
    db.create_all()
    user = create_test_user()
    return client, app_ctx, user


def clear_session(user, app_ctx):
    user.delete()
    db.session.remove()
    db.drop_all()
    app_ctx.pop()


@pytest.fixture(scope="session")
def client_with_user():
    client, app_ctx, user = prepare_user_and_client()
    yield client
    clear_session(user, app_ctx)


@pytest.fixture(scope="session")
def client_with_project():
    client, app_ctx, user = prepare_user_and_client()
    # create project
    resp = client.post("/api/auth", json=USER_CREDS)
    access_token = resp.json["data"]["access_token"]

    with open(CREATE_PROJECT_JSON_PATH, "r") as json_f:
        payload = json.load(json_f)
        resp = client.post(
            "/api/project",
            headers={"Authorization": f"Bearer {access_token}"},
            json=payload,
        )

        proj_id = resp.json["data"]["project"]["id"]
        project = Project.query.filter(Project.id == proj_id).first()

        client.project = project
        client.token = access_token

        yield client

    clear_session(user, app_ctx)
