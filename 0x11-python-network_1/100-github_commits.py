#!/usr/bin/python3
'''use git api and requests lib to print last 10 commits given user and repo'''
if __name__ == "__main__":
    import sys
    import requests

    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    r = requests.get(url).json()
    try:
        for i in range(10):
            print("{}: {}".format(
                  r[i].get('sha'),
                  r[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
