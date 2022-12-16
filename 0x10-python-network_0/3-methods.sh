#!/bin/bash
# Display all the HTTP methods server will be accepting
curl -sI -X OPTIONS "$1" | grep Allow | cut -d' ' -f1 --complement
