#!/usr/bin/env python3
import requests
import base64
from pprint import pprint


def get_creds():
    data = {
        'consumer_key': '.secrets/consumer.key',
        'consumer_secret': '.secrets/consumer.secret',
        'username': '.secrets/username',
        'password': '.secrets/password',
    }

    for key, val in data.items():
        with open(val) as f:
            data[key] = f.read().strip()

    token_combo = data['consumer_key'] + ':' + data['consumer_secret']
    data['basic_token'] = str(base64.b64encode(token_combo.encode('utf-8')),
                              'utf-8')
    data['grant_type'] = 'password'
    print(data)
    return data


def get_api(url='https://api.stubhub.com/login'):
    creds = get_creds()
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ' + creds['basic_token'],
    }
    data = {
        'username': creds['username'],
        'password': creds['password'],
        'grant_type': creds['grant_type']
    }
    r = requests.post(url, headers=headers, data=data)

    return r


if __name__ == '__main__':
    api = get_api()
    print(api.status_code, api.reason, api.text)
