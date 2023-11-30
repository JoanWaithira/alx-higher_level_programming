#!/bin/bash
# a Bash script that takes in a URL as an argument,
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
