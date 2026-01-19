#!/bin/sh

## Run this script to reinstall the MAF environment
## source reinstall.sh
deactivate && source .venv/bin/activate && uv add --prerelease=allow -r requirements.txt && uv sync;