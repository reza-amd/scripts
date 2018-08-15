# apt-get update && apt-get install -y emacs24-nox python3-numpy python3-dev python3-pip python3-wheel

# pip3 install setuptools --upgrade
# pip3 install protobuf --upgrade

# git config --locall user.email "deven.desai.amd@gmail.com"
# git config --local user.name "Deven Desai"


HOME=/root


# rm -rf $HOME/hcc/
# cd $HOME && git clone --recursive https://github.com/RadeonOpenCompute/hcc.git
# cd $HOME/hcc && git checkout -b issue812-fix d530be7
# cd $HOME/hcc && mkdir build && cd build && cmake -DCMAKE_BUILD_TYPE=Release .. && make package -j$(nproc) && dpkg -i *.deb


# rm -rf $HOME/HIP
# cd $HOME && git clone -b roc-1.8.x-pr457 https://github.com/parallelo/HIP.git 
# #cd $HOME && git clone -b roc-1.8.x-pr457-altfix https://github.com/deven-amd/HIP.git 
# cd $HOME/HIP && mkdir build && cd build && cmake .. && make package -j$(nproc) && dpkg -i *.deb


# apt-get update && apt-get install -y wget unzip libssl-dev libboost-dev libboost-system-dev libboost-filesystem-dev

# rm -rf $HOME/rocm-cmake
# cd $HOME && git clone https://github.com/RadeonOpenCompute/rocm-cmake.git 
# cd $HOME/rocm-cmake && mkdir build && cd build && cmake .. && make package -j$(nproc) && dpkg -i ./rocm-cmake*.deb

# rm -rf $HOME/MIOpenGEMM
# cd $HOME && git clone https://github.com/ROCmSoftwarePlatform/MIOpenGEMM.git
# cd $HOME/MIOpenGEMM &&  mkdir build && cd build && cmake .. && make package -j$(nproc) && dpkg -i ./miopengemm*.deb

# rm -rf $HOME/half
# cd $HOME &&  mkdir half && cd half && wget https://downloads.sourceforge.net/project/half/half/1.12.0/half-1.12.0.zip && unzip *.zip

# rm -rf $HOME/miopen
# #cd $HOME && git clone -b 1.4.x https://github.com/AMDComputeLibraries/MLOpen.git miopen
# #cd $HOME && git clone -b master https://github.com/ROCmSoftwarePlatform/MIOpen.git miopen
# cd $HOME && git clone -b pr1061-fix https://github.com/deven-amd/MIOpen.git miopen
cd $HOME/miopen && rm -rf build && mkdir build && cd build && \
    CXX=/opt/rocm/bin/hcc cmake \
       -DMIOPEN_BACKEND=HIP \
       -DCMAKE_PREFIX_PATH="/opt/rocm/hcc;/opt/rocm/hip" \
       -DCMAKE_CXX_FLAGS="-isystem /usr/include/x86_64-linux-gnu/" \
       -DHALF_INCLUDE_DIR=$HOME/half/include \
       -DCMAKE_BUILD_TYPE=Release \
       ..  && \
    make package -j$(nproc) && dpkg -i ./MIOpen*.deb


# version=0.15.0
# cd $HOME/
# wget https://github.com/bazelbuild/bazel/releases/download/$version/bazel-$version-installer-linux-x86_64.sh
# chmod a+x bazel-$version-installer-linux-x86_64.sh
# ./bazel-$version-installer-linux-x86_64.sh
