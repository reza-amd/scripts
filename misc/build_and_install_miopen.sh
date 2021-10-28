set -eux

# cd /root && git clone https://github.com/ROCmSoftwarePlatform/MIOpen
# cd /root && git clone https://github.com/AMDComputeLibraries/MLOpen


# MIOPEN=MIOpen
MIOPEN=MLOpen

cd /root/$MIOPEN


# git checkout miopen-develop-8b2f2602
# git checkout miopen-develop-7177b7c-bf16_1k-as-fp16-plus-jd-only-solver

# git remote add open_source https://github.com/ROCmSoftwarePlatform/MIOpen 
# git fetch open_source
# git config --global user.email "deven.desai.amd@gmail.com"
# git config --global user.name "Deven Desai"
# git config --global http.sslverify false
# git cherry-pick 374b32c7efd15a09f8c9a141169faa97d1c0b090

# ROCM_PATH=/opt/rocm-4.3.1/
ROCM_PATH=/opt/rocm-4.5.0/

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# cd /root/$MIOPEN
# apt-get update && apt-get install -y python3-venv
# cmake -P install_deps.cmake --minimum

cd /root/$MIOPEN
rm -rf build && mkdir build
cd build

export CXX=$ROCM_PATH/llvm/bin/clang++

cmake \
    -DMIOPEN_BACKEND=HIP \
    -DCMAKE_PREFIX_PATH="$ROCM_PATH/hip;$ROCM_PATH/;/usr/local" \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm/ \
    ..

# cmake --build . --config Release --target install
cmake --build . --config Release --target package
