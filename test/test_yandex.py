import pytest
import requests
from main import mkdir_ya

GOOD_TOKEN = 'BAR'
BAD_TOKEN = 'FOO'
BAD_URL = 'https://cloud-api.yandex.net/v1/disk/resourcess'


def setup():  # удаление ранее созданной папки, если таковая была
    ya_headers = {
        'Accept': 'application/json',
        'Authorization': GOOD_TOKEN
    }
    upload_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    folder_name = 'test'  # чтобы можно было сделать переменную
    dirname = '/' + folder_name
    ya_params = {'path': dirname}
    response = requests.delete(upload_url, params=ya_params, headers=ya_headers)
    return response.status_code


def test_created():  # нормальный
    assert mkdir_ya() == 201


def test_conflict():  # папка уже создана
    assert mkdir_ya() == 409


def test_unauthorized():  # ошибка авторизации
    token = BAD_TOKEN
    assert mkdir_ya(token) == 401


def test_not_found():  # ресурс не найден (неправильный урл)
    token = GOOD_TOKEN
    url = BAD_URL
    assert mkdir_ya(token, url) == 404



