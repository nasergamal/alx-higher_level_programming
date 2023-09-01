#!/usr/bin/python3
'''fetch x-request-id from header with request lib'''
if __name__ == "__main__":
    import sys
    import requests

    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
