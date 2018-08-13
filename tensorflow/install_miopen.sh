HOME=/home/rocm-user
SUDO_CMD=sudo

$SUDO_CMD apt-get update && $SUDO_CMD apt-get install -y wget unzip libssl-dev libboost-dev libboost-system-dev libboost-filesystem-dev

cd $HOME && git clone https://github.com/RadeonOpenCompute/rocm-cmake.git 
cd $HOME/rocm-cmake && $SUDO_CMD mkdir -p build && cd build && $SUDO_CMD cmake .. && $SUDO_CMD make package -j$(nproc) && $SUDO_CMD dpkg -i ./rocm-cmake*.deb

cd $HOME && git clone https://github.com/ROCmSoftwarePlatform/MIOpenGEMM.git
cd $HOME/MIOpenGEMM && $SUDO_CMD mkdir -p build && cd build && $SUDO_CMD cmake .. && $SUDO_CMD make package -j$(nproc) && $SUDO_CMD dpkg -i ./miopengemm*.deb

cd $HOME && $SUDO_CMD mkdir half && cd half && $SUDO_CMD wget https://downloads.sourceforge.net/project/half/half/1.12.0/half-1.12.0.zip && $SUDO_CMD unzip *.zip

#cd $HOME && git clone -b 1.4.x https://github.com/AMDComputeLibraries/MLOpen.git miopen
cd $HOME && git clone https://github.com/ROCmSoftwarePlatform/MIOpen.git miopen

cd $HOME/miopen && $SUDO_CMD rm -rf build && $SUDO_CMD mkdir build && cd build

$SUDO_CMD CXX=/opt/rocm/bin/hcc cmake \
       -DMIOPEN_BACKEND=HIP \
       -DCMAKE_PREFIX_PATH="/opt/rocm/hcc;/opt/rocm/hip" \
       -DCMAKE_CXX_FLAGS="-isystem /usr/include/x86_64-linux-gnu/" \
       -DHALF_INCLUDE_DIR=$HOME/half/include \
       -DCMAKE_BUILD_TYPE=Debug \
       .. 

$SUDO_CMD make package -j$(nproc)
#$SUDO_CMD make package -j$(nproc) && $SUDO_CMD dpkg -i ./MIOpen*.deb

#cd $HOME && git clone https://github.com/RadeonOpenCompute/clang-ocl.git
#cd $HOME/clang-ocl && $SUDO_CMD mkdir -p build && cd build && $SUDO_CMD cmake .. && $SUDO_CMD make package -j$(nproc) && $SUDO_CMD dpkg -i ./rocm-clang-ocl*.deb

