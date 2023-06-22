#!/bin/bash
# script displays only the status code returned from the server
curl -s -o /dev/null -w "%{http_code}" "$1"
