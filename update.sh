#!/bin/sh
docker build -t mikespub/quickstart-python:latest -f Dockerfile .
docker build -t mikespub/quickstart-python:alpine -f Dockerfile.alpine .
docker push mikespub/quickstart-python:latest
docker push mikespub/quickstart-python:alpine
