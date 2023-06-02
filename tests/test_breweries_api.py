import pytest
import requests
import random

BASE_URL = 'https://api.openbrewerydb.org/v1/breweries/'


def get_random_brewery_id():
    """Function get random brewery id"""

    response = requests.get(BASE_URL)
    data = response.json()
    random_brewery = random.choice(data)['id']

    return random_brewery


@pytest.mark.parametrize('random_id', [get_random_brewery_id(), get_random_brewery_id()],
                         ids=['first random id', 'second random id'])
def test_get_single_brewery(random_id):
    """Check get single brewery"""

    response = requests.get(BASE_URL + f'{random_id}')
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json['id'] == random_id


@pytest.mark.parametrize('city', ['New York', 'Denver'])
def test_get_brewery_by_city(city):
    """Check get brewery by city"""

    response = requests.get(url=BASE_URL, params={'by_city': city})
    resp_json = response.json()
    assert response.status_code == 200

    for brewery in resp_json:
        assert brewery['city'] == city


@pytest.mark.parametrize('input_amount, output_amount', [(1, 1), (50, 50), (51, 50)],
                         ids=['get breweries = 1', 'get breweries = 50', 'get breweries = 51'])
def test_get_random_brewery_with_size(input_amount, output_amount):
    """Check get random brewery with size"""

    response = requests.get(url=BASE_URL + 'random/', params={'size': input_amount})
    resp_json = response.json()
    assert response.status_code == 200
    assert len(resp_json) == output_amount


@pytest.mark.parametrize('input_amount, output_amount', [(50, 50), (200, 200), (201, 200)],
                         ids=['get brewery = 50', 'get brewery = 200', 'get brewery = 201'])
def test_get_brewery_per_page(input_amount, output_amount):
    """Check per_page"""

    response = requests.get(url=BASE_URL, params={'per_page': input_amount})
    resp_json = response.json()
    assert response.status_code == 200
    assert len(resp_json) == output_amount


def test_get_brewery_by_type_invalid_type():
    """Check err by_type"""

    response = requests.get(url=BASE_URL, params={'by_type': 'invalid_type'})
    resp_json = response.json()
    assert response.status_code == 400
    assert resp_json['errors'][0] == 'Brewery type must include one of these types: [' \
                                     '"micro", "nano", "regional", "brewpub", "large", "planning", ' \
                                     '"bar", "contract", "proprietor", "closed"]'
