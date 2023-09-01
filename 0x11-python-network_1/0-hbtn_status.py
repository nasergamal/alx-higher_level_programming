#!/usr/bin/python3
'''fetch site body'''

if __name__ == "__main__":
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        the_page = response.read()
    print('Body response:')
    print(f'\t- type: {type(the_page)}')
    print(f'\t- content: {the_page}')
    print(f'\t- utf8 content: {the_page.decode()}')
