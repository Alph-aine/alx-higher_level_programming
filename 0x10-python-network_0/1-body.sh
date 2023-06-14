#!/bin/bash
# script sends a get request to a web server and makes sure to follow any redirections
curl -sL "$1"
