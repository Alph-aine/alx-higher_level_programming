#!/bin/bash
# displays all http method a server would accept
curl -sI "$1" | grep 'Allow:' | cut -f2- -d' '
