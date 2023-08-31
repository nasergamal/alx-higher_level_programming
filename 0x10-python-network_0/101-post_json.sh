#!/bin/bash
# post json file
curl -H "Content-Type: application/json" -d "$(cat "$2")" -sL "$1"
