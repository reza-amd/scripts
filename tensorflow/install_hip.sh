rm -rf /root/HIP
cd /root/ && git clone https://github.com/ROCm-Developer-Tools/HIP.git
cd /root/HIP && mkdir build && cd build && cmake .. && make package -j$(nproc) && dpkg -i *.deb
