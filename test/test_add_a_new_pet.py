import requests
from hamcrest import assert_that, is_
from utils import test_data
from utils.test_data import host


class TestAddNewPet:

    def test_add_a_new_pet(self, data=test_data.random_pet):
        resp = requests.post(url=f"{host}/v2/pet", json=data, headers={
            'Content-type': 'application/json',
            'Accept': 'application/json'
        })
        assert_that(resp.status_code, is_(200))
        assert_that(resp.json()['id'], is_(data['id']))
        assert_that(resp.json()['name'], is_(data['name']))
        assert_that(resp.json()['status'], is_(data['status']))

    def test_add_a_new_pet_negative(self):
        data = {
            "id": "qwrqweqwe",
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        resp = requests.post(url=f"{host}/v2/pet", json=data, headers={
            'Content-type': 'application/json',
            'Accept': 'application/json'
        })
        assert_that(resp.status_code, is_(500))
