#!/bin/bash
# Takes in a URL, sends a POST request to the passed URL
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
