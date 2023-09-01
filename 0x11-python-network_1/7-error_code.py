#!/usr/bin/python3
'''print response body or error code'''
import sys
import requests

r = requests.get(sys.argv[1])
if r.status_code == requests.codes.ok:
    print(r.text)
else:
    print(r.status_code)
