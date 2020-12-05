#!/usr/bin/env bash
set -ex

# assumption is that this script is executed from  the root of the JAX repo 

python3 build/build.py

# python3 build/build.py --enable_cuda
# python3 build/build.py --enable_rocm


