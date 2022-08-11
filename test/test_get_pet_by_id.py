import requests
from utils import test_data
from hamcrest import assert_that, is_


class TestGetPetById:

    def test_get_pet_by_id(self, data=test_data.random_pet):
        requests.post(url="https://petstore.swagger.io/v2/pet", json=data, headers={
            'Content-type': 'application/json',
            'Accept': 'application/json'
        })
        resp = requests.get(url=f"https://petstore.swagger.io/v2/pet/{data['id']}")
        assert_that(resp.status_code, is_(200))
        assert_that(resp.json()['id'], is_(data['id']))
        assert_that(resp.json()['name'], is_('doggie'))
        assert_that(resp.json()['status'], is_('available'))

    def test_get_pet_by_id_negative(self, pet_id=142255125):
        resp = requests.get(url=f"https://petstore.swagger.io/v2/pet/{pet_id}")
        assert_that(resp.status_code, is_(404))
        assert_that(resp.json()['type'], is_('error'))
        assert_that(resp.json()['message'], is_('Pet not found'))
