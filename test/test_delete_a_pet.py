import requests
from hamcrest import assert_that, is_
from utils import test_data
from utils.test_data import host


class TestDeletePet:

    def test_delete_a_pet(self, data=test_data.random_pet):
        resp = requests.post(url=f"{host}/v2/pet", json=data, headers={
            'Content-type': 'application/json',
            'Accept': 'application/json'
        })
        assert_that(resp.status_code, is_(200))
        resp = requests.delete(url=f"{host}/v2/pet/{data['id']}")
        assert_that(resp.status_code, is_(200))
        resp = requests.get(url=f"{host}/v2/pet/{data['id']}")
        assert_that(resp.status_code, is_(404))
