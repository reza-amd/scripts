# Workaround: build HIP from source using fork that holds roc-1.8.x with merged PR457
rm -rf /root/HIP
cd /root/ && git clone -b roc-1.8.x-pr457 https://github.com/parallelo/HIP.git 
#cd /root/ && git clone https://github.com/deven-amd/HIP.git
cd /root/HIP && mkdir -p build && cd build && cmake .. && make package -j$(nproc) && dpkg -i *.deb
