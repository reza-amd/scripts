# rm -rf /root/hcc/
# cd /root
# git clone --recursive https://github.com/RadeonOpenCompute/hcc.git
# cd /root/hcc && mkdir build && cd build && cmake -DCMAKE_BUILD_TYPE=Release .. && make


# rm -rf /root/HIP
# cd /root/ && git clone https://github.com/deven-amd/HIP.git
# cd /root/HIP && mkdir build && cd build && cmake -DHCC_HOME=/root/hcc/build .. && make package -j$(nproc) && dpkg -i *.deb
