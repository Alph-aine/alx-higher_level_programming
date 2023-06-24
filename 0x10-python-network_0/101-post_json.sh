#!/bin/bash
# posts a  json data to server
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
