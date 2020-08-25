#!/usr/bin/python3
"""Fetches URL"""
import requests


if __name__ == "__main__":
    x = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(x.text))
    print('\t- content:', x.text)
