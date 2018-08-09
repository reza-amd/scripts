rm -rf /root/HIP
cd /root/ && git clone -b roc-1.8.x-pr457-altfix https://github.com/deven-amd/HIP.git 
cd /root/HIP && mkdir build && cd build && cmake .. && make package -j$(nproc) && dpkg -i *.deb
