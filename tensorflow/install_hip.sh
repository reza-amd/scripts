# rm -rf /root/HIP
#
# cd /root/ && git clone https://github.com/ROCm-Developer-Tools/HIP.git
#

build_type=Release
# build_type=Debug

cd /root/HIP && \
    rm -rf build && mkdir build && cd build && \
    cmake -DCMAKE_BUILD_TYPE=$build_type .. && \
    make package -j$(nproc) && dpkg -i *.deb
