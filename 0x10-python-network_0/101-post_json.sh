#!/bin/bash
# Sends JSON POST request and then will display its body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
