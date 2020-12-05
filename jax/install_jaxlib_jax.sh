#!/usr/bin/env bash
set -ex

# assumption is that this script is executed from  the root of the JAX repo 

pip3 install dist/*.whl  # installs jaxlib (includes XLA)
pip3 install -e .  # installs jax
