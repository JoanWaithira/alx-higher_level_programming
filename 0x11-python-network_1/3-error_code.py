#!/usr/bin/python3
""" a Python script that takes in a URL """

from urllib import request, error
import sys

if __name__ == '__main__':
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
