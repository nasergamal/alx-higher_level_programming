#!/usr/bin/python3
'''print search result'''
import sys
import requests

q = ""
if len(sys.argv) > 1:
    q = sys.argv[1]

r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
try:
    r = r.json()
    if not r or r == {}:
        print('No result')
    else:
        print(f"[{r['id']}] {r['name']}")
except Exception as e:
    print("Not a valid JSON")
