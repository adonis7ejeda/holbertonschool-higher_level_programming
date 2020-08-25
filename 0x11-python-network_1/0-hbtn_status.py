#!/usr/bin/python3
"""Fetches URL"""
from urllib import request


if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as resp:
        x = resp.read()
        print('Body response:')
        print('\t- type: ', end='')
        print(type(x))
        print('\t- content: ', end='')
        print(x)
        print('\t- utf8 content: ' + x.decode('utf-8'))
