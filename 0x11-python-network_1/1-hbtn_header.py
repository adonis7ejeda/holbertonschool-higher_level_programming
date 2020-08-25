#!/usr/bin/python3
"""Display value X-Request-Id"""
from urllib import request
import sys


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as resp:
        print(resp.headers['X-Request-Id'])
