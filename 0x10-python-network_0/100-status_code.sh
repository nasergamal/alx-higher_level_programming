#!/bin/bash
# print status code 
curl -X GET -sIw "%{http_code}" "$1" -o /dev/null
