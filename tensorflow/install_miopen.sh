cd /root && git clone -b 1.4.x https://github.com/AMDComputeLibraries/MLOpen.git miopen
    
cd /root/miopen && cmake -P install_deps.cmake --prefix /usr/miopen-deps

apt-get update && apt-get install -y libssl-dev libboost-dev libboost-system-dev libboost-filesystem-dev

rm -rf build && mkdir build && cd build

CXX=/opt/rocm/bin/hcc cmake \
       -DMIOPEN_BACKEND=HIP \
       -DCMAKE_PREFIX_PATH="/opt/rocm/hcc;/opt/rocm/hip" \
       -DCMAKE_CXX_FLAGS="-isystem /usr/include/x86_64-linux-gnu/" \
       -DMIOPEN_MAKE_BOOST_PUBLIC=on \
       -DCMAKE_BUILD_TYPE=Debug \
       .. 

make install -j$(nproc)
