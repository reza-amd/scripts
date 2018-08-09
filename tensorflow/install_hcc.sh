rm -rf /root/hcc/
cd /root && git clone --recursive https://github.com/RadeonOpenCompute/hcc.git
cd /root/hcc && git checkout -b issue812-fix d530be7
cd /root/hcc && mkdir build && cd build && cmake -DCMAKE_BUILD_TYPE=Release .. && make package -j$(nproc) && dpkg -i *.deb


