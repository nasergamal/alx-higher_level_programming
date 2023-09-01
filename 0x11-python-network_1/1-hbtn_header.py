#!/usr/bin/python3
'''fetch x-request-id from site's hearder'''

if __name__ == "__main__":
    import sys
    import urllib.request
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers['X-Request-Id'])
