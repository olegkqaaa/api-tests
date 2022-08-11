import requests
from utils import test_data
from utils.test_data import host
from hamcrest import assert_that, is_


class TestUpdatePet:

    def test_update_a_pet(self, data=test_data.random_pet):
        requests.post(url=f"{host}/v2/pet", json=data, headers={
            'Content-type': 'application/json',
            'Accept': 'application/json'
        })
        data['name'] = 'cat'
        resp = requests.put(url=f"{host}/v2/pet", json=data, headers={
            'Content-type': 'application/json',
            'Accept': 'application/json'
        })
        assert_that(resp.status_code, is_(200))
        assert_that(resp.json()['name'], is_('cat'))
