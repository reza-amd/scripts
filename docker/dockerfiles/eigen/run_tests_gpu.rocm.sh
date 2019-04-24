#!/bin/bash

EIGEN_DIR=/home/rocm-user/eigen
# EIGEN_DIR=/home/rocm-user/GIT_MIRROR/eigen
# EIGEN_DIR=/home/rocm-user/ROCM_FORK/eigen

cd $EIGEN_DIR && hg pull -u


cd $EIGEN_DIR && rm -rf build && mkdir build
cd $EIGEN_DIR/build && cmake -DEIGEN_TEST_CXX11=ON -DEIGEN_TEST_HIP=ON ..
cd $EIGEN_DIR/build && ./check.sh "gpu|cxx11_tensor_device"

