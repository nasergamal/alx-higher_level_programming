#!/bin/bash
# post json file
curl -d "$2" -X POST -sL "$1"
