#!/bin/bash
# script send a POST request to the passed url and displays the body of the response
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
