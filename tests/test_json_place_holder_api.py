import pytest
import requests

BASE_URL = 'https://jsonplaceholder.typicode.com/'


@pytest.mark.parametrize('post_num_id', [1, 100], ids=['post_num_id = 1', 'post_num_id = 100'])
def test_get_posts_by_id(post_num_id):
    """Check get posts by id"""

    response = requests.get(BASE_URL + f'posts/{post_num_id}')
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json['id'] == post_num_id


def test_get_all_posts():
    """Check get all posts"""

    response = requests.get(BASE_URL + 'posts')
    resp_json = response.json()
    assert response.status_code == 200
    assert len(resp_json) == 100


@pytest.mark.parametrize('user_id', [1, 10], ids=['user_id = 1', 'user_id = 10'])
def test_get_users_by_id(user_id):
    """Check get users by id"""

    response = requests.get(BASE_URL + f'users/{user_id}')
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json['id'] == user_id


@pytest.mark.parametrize('album_id', [1, 100], ids=['album_id = 1', 'album_id = 100'])
def test_get_albums_by_id(album_id):
    """Check get albums by id"""

    response = requests.get(BASE_URL + f'albums/{album_id}')
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json['id'] == album_id


def test_get_posts_by_invalid_id():
    """Check response by invalid post_id"""

    response = requests.get(BASE_URL + 'posts/101')
    assert response.status_code == 404
