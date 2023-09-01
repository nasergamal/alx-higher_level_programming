#!/usr/bin/python3
'''use git api and requests lib to auth and get id'''
import sys
import requests

r = requests.get('https://api.github.com/user', auth=(sys.argv[1], sys.argv[2]))
try:
    print(r.json()['id'])
except KeyError:
    print("None")
