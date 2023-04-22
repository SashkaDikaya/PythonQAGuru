import requests
from pprint import pprint

from requests import Response
from voluptuous import Schema, PREVENT_EXTRA
from pytest_voluptuous import S
from utils.base_session import reqres_session


#жесткая схема
create_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    },
    required=True, #все поля обязательно должны вывестись с ответе
    extra=PREVENT_EXTRA #все перечисленные поля это единственные поля которые должны прийти в ответе, ничего дополнительно быть не может
)

#схема где все поля не обязтельные, но мы указывает вот какое точно должно быть
'''create_user_schema = Schema(
    {
        Required("name"): str, #обязательно только вот это поле
        "job": str,
        "id": str,
        "createdAt": str
    },
    required=False,
    extra=PREVENT_EXTRA #все перечисленные поля это единственные поля которые должны прийти в ответе, ничего дополнительно быть не может
)'''

#схема где все поля обязтельные, но мы указывает вот какое может и не быть обязательным
'''create_user_schema = Schema(
    {
        "name": str, #обязательно только вот это поле
        Optional("job"): str,
        "id": str,
        "createdAt": str
    },
    required=True,
    extra=PREVENT_EXTRA #все перечисленные поля это единственные поля которые должны прийти в ответе, ничего дополнительно быть не может
)'''

def test_create_user_schema():
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
    assert result.json() == S(create_user_schema)


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
    assert result.json() == S(create_user_schema)