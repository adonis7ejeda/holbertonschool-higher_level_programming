#!/usr/bin/python3
"""Sends a request and display body response"""
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('utf-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
