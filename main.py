import requests

YANDEX_TOKEN = 'BAR'
URL = 'https://cloud-api.yandex.net/v1/disk/resources'


def mkdir_ya(token=YANDEX_TOKEN, upload_url=URL):
    ya_headers = {
        'Accept': 'application/json',
        'Authorization': token
    }
    folder_name = 'test'  # чтобы можно было сделать переменную
    dirname = '/' + folder_name
    ya_params = {'path': dirname}
    response = requests.put(upload_url, params=ya_params, headers=ya_headers)
    status_code = response.status_code
    msg = {201: 'created', 401: 'unauthorized', 404: 'not_found', 409: 'conflict'}
    print(f'{status_code}, {msg.get(status_code)}')
    return status_code


if __name__ == '__main__':
    mkdir_ya()

