#!/usr/bin/env bash
set -ex

# cd $HOME
# git clone https://github.com/inailuig/tensorflow/ inailuig-tf
# cd $HOME/inailuig-tf
# git checkout jax-rocm-gpukernels

cd $HOME
git clone https://github.com/ROCmSoftwarePlatform/tensorflow-upstream rocm-tf
cd $HOME/rocm-tf
git checkout develop-upstream-deven-rocsolver

# cd $HOME/jax
# git remote add inailuig https://github.com/inailuig/jax
# git fetch inailuig
# git checkout inailuig/rocm-gpukernels
