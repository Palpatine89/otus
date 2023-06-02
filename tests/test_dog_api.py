import pytest
import requests
import random
from jsonschema import validate

BASE_URL = 'https://dog.ceo/api/'


def get_random_breed():
    """Function get random breed"""

    response = requests.get('https://dog.ceo/api/breeds/list/all')
    data = response.json()['message']
    random_breed = random.choice(list(data.keys()))

    return random_breed


@pytest.mark.parametrize('input_amount, output_amount', [(1, 1), (50, 50), (51, 50)],
                         ids=['get image = 1', 'get image = 50', 'get image = 51'])
def test_get_random_dog_image(input_amount, output_amount):
    """Check get random image"""

    response = requests.get(BASE_URL + f'breeds/image/random/{input_amount}')
    resp_json = response.json()
    assert response.status_code == 200
    assert len(resp_json['message']) == output_amount
    assert resp_json['status'] == 'success'


def test_dog_api_json_schema():
    """Check dog api schema"""

    response = requests.get(BASE_URL + 'breeds/image/random')
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }

    validate(instance=response.json(), schema=schema)


def test_get_image_by_breed():
    """Check get image by breed"""

    random_breed = get_random_breed()
    response = requests.get(BASE_URL + f'breed/{random_breed}/images')
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json['status'] == 'success'


def test_by_breed_invalid_value():
    """Check invalid breed"""

    response = requests.get(BASE_URL + 'breed/test/images')
    resp_json = response.json()
    assert response.status_code == 404
    assert resp_json['message'] == 'Breed not found (master breed does not exist)'
    assert resp_json['status'] == 'error'


@pytest.mark.parametrize('breed, sub_breed, amount',
                         [('bulldog', 'boston', 1),
                          ('bulldog', 'english', 1),
                          ('hound', 'afghan', 1),
                          ('hound', 'ibizan', 1)])
def test_by_sub_breed_random_multiple_images(breed, sub_breed, amount):
    """Check get image by sub-breed"""

    response = requests.get(BASE_URL + f'breed/{breed}/{sub_breed}/images/random/{amount}')
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json['status'] == 'success'
