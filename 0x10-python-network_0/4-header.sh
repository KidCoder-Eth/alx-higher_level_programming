#!/bin/bash
# Send a GET request and then will be displaying its body as a response
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
