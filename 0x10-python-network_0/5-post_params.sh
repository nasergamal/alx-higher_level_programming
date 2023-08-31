#!/bin/bash
# post parameters
curl -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST -sL "$1"
