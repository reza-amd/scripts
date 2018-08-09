rm -rf /root/hcc/
cd /root && git clone --recursive https://github.com/RadeonOpenCompute/hcc.git
cd /root/hcc && git checkout -b issue812-fix d530be7
cd /root/hcc && mkdir build && cd build && cmake -DCMAKE_BUILD_TYPE=Release .. && make package -j$(nproc) && dpkg -i *.deb


rm -rf /root/HIP
#cd /root/ && git clone -b roc-1.8.x-pr457 https://github.com/parallelo/HIP.git 
cd /root/ && git clone -b roc-1.8.x-pr457-altfix https://github.com/deven-amd/HIP.git 
cd /root/HIP && mkdir build && cd build && cmake .. && make package -j$(nproc) && dpkg -i *.deb
