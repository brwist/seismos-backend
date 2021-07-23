import json
from .utils import USER_CREDS


def test_auth(client_with_user):
    resp = client_with_user.post("/api/auth", json=USER_CREDS)
    assert resp
    assert resp.status_code == 200
    assert resp.json
    assert resp.json["status"] == 200
    assert resp.json["message"] == "Login Successful"
    assert resp.json["data"]["access_token"]

    access_token = resp.json["data"]["access_token"]
    resp = client_with_user.get("/api/auth", headers={"Authorization": f"Bearer {access_token}"})
    assert resp
    assert resp.status_code == 200
    assert resp.json
    assert resp.json["status"] == 200
    assert resp.json["message"] == "User details"
    assert resp.json["data"]["user"]


def test_project_endpoint(client_with_user):
    resp = client_with_user.post("/api/auth", json=USER_CREDS)
    access_token = resp.json["data"]["access_token"]

    create_project_json_path = "tests/static/project_create.json"

    with open(create_project_json_path, "r") as json_f:
        payload = json.load(json_f)
        assert payload
        resp = client_with_user.post(
            "/api/project",
            headers={"Authorization": f"Bearer {access_token}"},
            json=payload,
        )

        assert resp.status_code == 200
        assert resp.json
        assert resp.json["message"] == "Project created successfully!"
        assert resp.json["status"] == 200
        assert resp.json["data"]
        assert resp.json["data"]["project"]
