#!/bin/bash
# print allowed requests
curl -sI "$1" | grep -i Allow | cut -d " " -f2-
