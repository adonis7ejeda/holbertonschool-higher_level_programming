#!/usr/bin/python3
"""Takes in a letter and sends a POST request"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = {'q': sys.argv[1]}
    else:
        q = {'q': ""}
    x = requests.post('http://0.0.0.0:5000/search_user', q)
    try:
        json_dict = x.json()
        if len(json_dict) == 2:
            print('[{}] {}'.format(json_dict.get('id'), json_dict.get('name')))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
