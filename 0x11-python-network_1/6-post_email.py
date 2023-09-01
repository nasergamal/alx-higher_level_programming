#!/usr/bin/python3
'''print response after a POST request with requests lib'''
if __name__ == "__main__":
    import sys
    import requests

    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
