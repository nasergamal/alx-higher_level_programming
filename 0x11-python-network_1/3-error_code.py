#!/usr/bin/python3
'''print site body or received error code'''
if __name__ == "__main__":
    import sys
    import urllib.request
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode())
    except urllib.error.URLError as e:
        print(f'Error code: {e.code}')
