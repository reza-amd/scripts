#!/usr/bin/env bash
set -ex

# assumption is that this script is executed from  the root of the JAX repo 

# Add the following option, to the "python3 build/build.py ... " command,
# to use a custom TF repo (instead of the TF repo specified in WORKSPACE)
#
# --bazel_options=--override_repository=org_tensorflow=<TF_repo_root_dir>


# # build jaxlib without GPU support
# python3 build/build.py

# # build jaxlib with CUDA GPU support
# python3 build/build.py --enable_cuda

# build jaxlib with ROCm GPU support
# python3 build/build.py --enable_rocm
python3 build/build.py --enable_rocm --bazel_options=--override_repository=org_tensorflow=/home/rocm-user/inailuig-tf
