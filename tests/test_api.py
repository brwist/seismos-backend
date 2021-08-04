import os
import io
import json
from .utils import USER_CREDS, TEST_STATIC_ROOT
from app.models import Project
from uuid import uuid4


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

    create_project_json_path = f"{TEST_STATIC_ROOT}/project_create.json"

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

        project = Project.query.filter(
            Project.id == resp.json["data"]["project"]["id"]
        ).first()

        # project data test
        assert project
        assert project.project_name == payload["projectValues"]["project_name"]
        assert project.project_uuid == payload["projectValues"]["project_uuid"]

        # equipment test
        assert project.equipment
        assert project.equipment.trailer_id == payload["equipmentValues"]["trailers_id"]
        assert project.equipment.powerpack_id == payload["equipmentValues"]["powerpack_id"]
        assert project.equipment.source_id == payload["equipmentValues"]["source_id"]
        assert project.equipment.accumulator_id == payload["equipmentValues"]["accumulator_id"]
        assert project.equipment.hydrophones_id == payload["equipmentValues"]["hydrophones_id"]
        assert project.equipment.transducer_id == payload["equipmentValues"]["transducer_id"]
        assert project.equipment.hotspot_id == payload["equipmentValues"]["hotspot_id"]

        # client test
        assert project.client
        assert project.client.password == payload["clientInfoValues"][0]["password"]
        assert project.client.title == payload["clientInfoValues"][0]["title"]
        assert project.client.client_name == payload["padInfoValues"]["client_name"]
        assert project.client.project_id == project.id
        assert project.client.operator_name == payload["padInfoValues"]["operator_name"]
        assert project.client.service_company_name == payload["padInfoValues"]["service_company_name"]
        assert project.client.wireline_company == payload["padInfoValues"]["wireline_company"]

        # client customer field

        # Pad test
        assert project.pad.pad_name == payload["padInfoValues"]["pad_name"]
        assert project.pad.number_of_wells == len(payload["wellInfoValues"])
        assert project.pad.number_of_wells == len(project.pad.wells)

        # Job test
        assert project.job_info.job_id == payload["jobInfoValues"]["job_id"]
        assert project.job_info.job_name == payload["jobInfoValues"]["job_name"]
        assert project.job_info.afe_id == payload["jobInfoValues"]["afe_id"]
        assert int(project.job_info.job_start_date.timestamp()) == payload["jobInfoValues"]["job_start_date"]
        assert int(project.job_info.job_end_date.timestamp()) == payload["jobInfoValues"]["job_end_date"]
        assert project.job_info.job_type
        assert project.job_info.job_type.value == payload["jobInfoValues"]["job_type"]
        assert project.job_info.location
        assert project.job_info.location.country_name.county_name == payload["jobInfoValues"]["country_name"]
        assert project.job_info.location.basin_name.basin_name == payload["jobInfoValues"]["basin_name"]
        assert project.job_info.location.state.value == payload["jobInfoValues"]["state"]

        # Crew test
        assert project.project_crew
        assert len(project.project_crew) == len(payload["crewInfoValues"])


def test_input_data_endpoint(client_with_user):
    resp = client_with_user.post("/api/auth", json=USER_CREDS)
    access_token = resp.json["data"]["access_token"]

    assert access_token

    filename = f"{str(uuid4())}.jpg"
    data = {
        "file": (io.BytesIO(b"abcdef"), filename)
    }

    file_path = f"static/{filename}"

    resp = client_with_user.post(
        "/api/input-data",
        headers={"Authorization": f"Bearer {access_token}"},
        content_type='multipart/form-data',
        data=data,
    )

    assert resp.status_code == 200

    with open(file_path) as uploaded_file:
        assert uploaded_file
        os.remove(file_path)

    input_data = {
        "project_id": 0,
        "well_id": 0,
    }

    resp = client_with_user.get(
        "/api/input-data",
        headers={"Authorization": f"Bearer {access_token}"},
        json=input_data
    )

    assert resp
    assert resp.json
    assert resp.json["status"]
    assert resp.json["message"]
    assert resp.json["message"] == "Data input details"
    assert resp.json["data"]
    assert resp.json["data"]["data_input"]

    data_input_field = ("hydrophone", "pumping_data", "pressure", "survey", "gamma_ray", "mud_log")
    for field in data_input_field:
        assert resp.json["data"]["data_input"][field]
        assert "file" in resp.json["data"]["data_input"][field]
        assert resp.json["data"]["data_input"][field]["file"]


def test_daily_log(client_with_user):
    resp = client_with_user.post("/api/auth", json=USER_CREDS)
    access_token = resp.json["data"]["access_token"]

    create_project_json_path = f"{TEST_STATIC_ROOT}/project_create.json"

    with open(create_project_json_path, "r") as json_f:
        payload = json.load(json_f)
        assert payload
        resp = client_with_user.post(
            "/api/project",
            headers={"Authorization": f"Bearer {access_token}"},
            json=payload,
        )

        assert resp
        assert resp.status_code == 200

        proj_id = resp.json["data"]["project"]["id"]
        assert proj_id

        project = Project.query.filter(Project.id == proj_id).first()
        assert project
        assert project.pad.wells
        well = project.pad.wells[0]
        assert well

        create_logs_static_path = f"{TEST_STATIC_ROOT}/daily_logs_create.json"

        with open(create_logs_static_path, "r") as json_f:
            logs = json.load(json_f)
            assert logs

            for log in logs:
                assert log

            payload = {
                "logs": logs,
                "project_id": 0,
                "well_id": well.id
            }

        assert resp


def test_default_value(client_with_user):
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
        proj_id = resp.json["data"]["project"]["id"]
        project = Project.query.filter(Project.id == proj_id).first()
        assert project
        assert project.pad.wells
        well = project.pad.wells[0]
        assert well
        with open("tests/static/default_value_create.json", "r") as f_json:
            default_values = json.load(f_json)
            assert default_values
            resp = client_with_user.put(
                f"/api/default-value/{well.id}",
                headers={"Authorization": f"Bearer {access_token}"},
                json=default_values,
            )

            assert resp.status_code == 200
            assert resp.json["msg"] == "Well's default value has been updated"

            resp = client_with_user.get(
                f"api/default-value/{well.id}",
                headers={"Authorization": f"Bearer {access_token}"}
            )

            assert resp.status_code == 200
            for key, value in default_values.items():
                assert key in resp.json
                assert value == resp.json[key]
