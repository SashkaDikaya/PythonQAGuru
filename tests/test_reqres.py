import requests
from requests import Response
from pprint import pprint

def test_get_users():
    result: Response = requests.get(
        "https://reqres.in/api/users",
        params={"page": 0},
        headers={"Authorization": "Token" },
        data={"a": "b"}
        #json={"a": "b"} если сервер не принимает json то меняем на data и будет выглядеть вот так data={"a": "b"}
    )

    print(result.status_code)
    pprint(result.request.headers)
    assert result.status_code == 200
    assert result.json()["page"] == 1
    assert len(result.json()["data"]) != 0

def test_create_user():
    name = "morpheus_1"
    job = "leader"

    result = requests.post(
        url="https://reqres.in/api/users",
        json={
            "name": name,
            "job": job
        }
    )

    pprint(result.json())
    assert result.status_code == 201
    assert result.json()["name"] == name
    assert result.json()["job"] == job
    assert isinstance(result.json()["id"], str)
    assert result.json()["createdAt"] == 0