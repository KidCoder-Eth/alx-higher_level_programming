#!/bin/bash
# Receives URL,then it will display size of the response
curl -sI "$1" | grep Content-Length | cut -d' ' -f2
