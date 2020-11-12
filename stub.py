#!/usr/bin/env python3
import requests
import base64
import json
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
    print(data)
    return data


def get_api():
    creds = get_creds()
    url = 'https://api.stubhub.com/sellers/oauth/accesstoken?grant_type='
    url += 'client_credentials'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + creds['basic_token'],
    }
    data = {
        'username': creds['username'],
        'password': creds['password']
    }
    r = requests.post(url, headers=headers, json=data)

    return r


if __name__ == '__main__':
    api = get_api()
    print(api.status_code, api.reason, api.text)
