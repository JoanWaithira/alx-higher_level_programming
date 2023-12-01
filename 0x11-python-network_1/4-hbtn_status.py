#!/usr/bin/python3
""" Write a Python script that fetches https://alx-intranet.hbtn.io/status """

import requests


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    r = requests.get(url)
    t = r.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))
