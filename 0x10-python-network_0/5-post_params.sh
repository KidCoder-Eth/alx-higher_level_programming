#!/bin/bash
# Send POST request and then display its body as response
curl -s -X POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
