import json
import pytest
from flask import current_app
from app.models import User
from app import create_app, db

USER_CREDS = {
    "username": "bobo",
    "password": "1234",
}

@pytest.fixture
def client():
    app = create_app(environment="testing")

    with app.test_client() as client:
        app_ctx = app.app_context()
        app_ctx.push()
        db.drop_all()
        db.create_all()
        user = User(
            username=USER_CREDS["username"],
            password=USER_CREDS["password"],
            email=f"{USER_CREDS['username']}@gmail.com"
        )
        user.save()
        yield client
        user.delete()
        db.session.remove()
        db.drop_all()
        app_ctx.pop()


def test_auth(client):
    resp = client.post("/api/auth", json=USER_CREDS)
    assert resp
    assert resp.status_code == 200
    assert resp.json
    assert resp.json["status"] == 200
    assert resp.json["message"] == "Login Successful"
    assert resp.json["data"]["access_token"]

    access_token = resp.json["data"]["access_token"]
    resp = client.get("/api/auth", headers={"Authorization": f"Bearer {access_token}"})
    assert resp
    assert resp.status_code == 200
    assert resp.json
    assert resp.json["status"] == 200
    assert resp.json["message"] == "User details"
    assert resp.json["data"]["user"]


def test_project(client):
    resp = client.post("/api/auth", json=USER_CREDS)
    access_token = resp.json["data"]["access_token"]

    create_project_json_path = "tests/static/project_create.json"

    with open(create_project_json_path, "r") as json_f:
        payload = json.load(json_f)
        assert payload
        resp = client.post("/api/project", headers={"Authorization": f"Bearer {access_token}"}, data=payload)
        assert resp.status_code == 200
        assert resp.json
        assert resp.json["message"] == "Project created successfully!"
        assert resp.json["status"] == 200
        assert resp.json["data"]
        assert resp.json["data"]["project"]
        # TODO check db for creating project
        # TODO get project by id
