#!/bin/bash
# sends a get request to a server with a header variable and a value
curl -sH "X-School-User-Id: 98" "$1"
