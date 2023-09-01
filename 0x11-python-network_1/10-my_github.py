#!/usr/bin/python3
'''use git api and requests lib to auth and get id'''
if __name__ == "__main__":
    import sys
    import requests

    basic = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get('https://api.github.com/user', auth=basic)
    print(r.json().get('id'))
