#!/bin/bash
# Send a request and then will display the status code
curl -s -L -I "$1" -o /dev/null -w '%{http_code}'
