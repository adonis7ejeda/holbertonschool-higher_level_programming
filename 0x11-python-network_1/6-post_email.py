#!/usr/bin/python3
"""POST with email"""
import requests
import sys


if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    x = requests.post(sys.argv[1], email)
    print(x.text)
