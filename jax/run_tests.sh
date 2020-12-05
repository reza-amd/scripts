#!/usr/bin/env bash
set -ex

# assumption is that this script is executed from  the root of the JAX repo 

python3 -m pytest -n auto tests
