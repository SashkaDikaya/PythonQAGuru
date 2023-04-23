from pytest_voluptuous import S
from requests import Response
from schemas.reqres import CREATE_USER_SCHEMA
from utils.base_session import reqres_session


def test_create_user_schema_v2():
    name = "morpheus_1"
    job = "leader"

    result: Response = reqres_session().post(
        url="/api/users",
        json={
            "name": name,
            "job": job
        }
    )

    print(result.text)
    assert result.status_code == 201
    assert result.json()["name"] == name
    assert result.json()["job"] == job
    assert isinstance(result.json()["id"], str)
    assert result.json() == S(CREATE_USER_SCHEMA)