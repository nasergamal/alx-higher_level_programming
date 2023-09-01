#!/usr/bin/python3
'''POST'''
import sys
import urllib.request
import urllib.parse

data = urllib.parse.urlencode({'email': sys.argv[2]})
data = data.encode('ascii')
with urllib.request.urlopen(sys.argv[1], data) as response:
    the_page = response.read().decode()
print(the_page)
