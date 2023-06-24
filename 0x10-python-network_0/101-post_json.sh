#!/bin/bash
# posts a  json data to server
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
