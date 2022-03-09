import requests
import configparser

config = configparser.ConfigParser()

config.read('../env.cfg')

headers = {
    "Authorization": f"Bearer {config['API']['SECRET_KEY']}",
    "Content-Type": "application/json"
}


def get_request(path, *args, **kwargs):
    return requests.get(
        f'{config["API"]["BASE_URL"]}{path}',
        headers=headers,
        *args,
        **kwargs
    )


def post_request(path, data, *args, **kwargs):
    return requests.post(
        f'{config["API"]["BASE_URL"]}{path}',
        headers=headers,
        data=data,
        *args,
        **kwargs
    )


if __name__ == '__main__':
    try:
        response = get_request('plan',)
        print(response.json())
    except requests.ConnectionError as httperr:
        print('Invalid URL', httperr)
    except Exception as e:
        print(e)
