#!/bin/sh
#
# Enable provenance and SBOM - see https://earthly.dev/blog/containerd-docker/
#
docker build --provenance=true --sbom=true -t mikespub/quickstart-python:latest -f Dockerfile .
docker build --provenance=true --sbom=true -t mikespub/quickstart-python:alpine -f Dockerfile.alpine .
docker push mikespub/quickstart-python:latest
docker push mikespub/quickstart-python:alpine
