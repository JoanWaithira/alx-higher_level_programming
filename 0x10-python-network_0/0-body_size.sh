#!/bin/bash
# Takes in a URL, send a requests and displays the size of the body
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
