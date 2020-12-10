#!/usr/bin/env bash
set -ex

# assumption is that this script is executed from  the root of the JAX repo 

# Add the following option, to the "python3 build/build.py ... " command,
# to use a custom TF repo (instead of the TF repo specified in WORKSPACE)
#
# --bazel_options=--override_repository=org_tensorflow=<TF_repo_root_dir>


options=""
# options="--enable_cuda"
options="--enable_rocm"
# options="$options --bazel_options=--subcommands"
options="$options --bazel_options=--override_repository=org_tensorflow=/home/rocm-user/rocm-tf"
# options="$options --bazel_options=--override_repository=org_tensorflow=/home/rocm-user/inailuig-tf"

python3 build/build.py $options
