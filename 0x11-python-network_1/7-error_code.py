#!/usr/bin/python3
"""Sends request and display body response"""
import requests
from requests.exceptions import HTTPError
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        print(resp.text)
    except HTTPError as e:
        print('Error code:', resp.status_code)
