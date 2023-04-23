import requests
from pytest_voluptuous import S
from requests import Response
from schemas.reqres import CREATE_USER_SCHEMA, UNKNOWN_LIST_SCHEMA
from utils.base_session import reqres_session


def test_unknown_list_schema():
    result = reqres_session().get('/api/unknown')
    assert result.json() == S(UNKNOWN_LIST_SCHEMA)