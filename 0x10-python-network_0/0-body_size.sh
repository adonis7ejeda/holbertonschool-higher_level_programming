#!/bin/bash
# Takes in a URL, sends a request to that URL
curl -sI  "$1" | grep -i Content-Length | grep -o '[0-9]\+'
