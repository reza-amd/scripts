#!/bin/bash

cd /root/eigen && \
    hg pull -u && \
    mkdir build && \
    cd build && \
    cmake -DEIGEN_TEST_CXX11=ON -DEIGEN_TEST_CUDA=ON .. &&
    ctest -D Nightly

