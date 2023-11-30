#!/bin/bash
# A bash script that takes in a URL, send a reques
curl -s "$1" | wc -c
