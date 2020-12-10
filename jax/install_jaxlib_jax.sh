#!/usr/bin/env bash
set -ex

# assumption is that this script is executed from  the root of the JAX repo 

sudo pip3 install --force-reinstall dist/*.whl  # installs jaxlib (includes XLA)
sudo pip3 install --force-reinstall -e .  # installs jax
