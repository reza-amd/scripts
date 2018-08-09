apt-get update && apt-get install -y emacs24-nox python3-numpy python3-dev python3-pip python3-wheel

pip3 install setuptools --upgrade
pip3 install protobuf --upgrade

git config --locall user.email "deven.desai.amd@gmail.com"
git config --local user.name "Deven Desai"

rm -rf /root/hcc/
cd /root && git clone --recursive https://github.com/RadeonOpenCompute/hcc.git
cd /root/hcc && git checkout -b issue812-fix d530be7
cd /root/hcc && mkdir build && cd build && cmake -DCMAKE_BUILD_TYPE=Release .. && make package -j$(nproc) && dpkg -i *.deb

rm -rf /root/HIP
cd /root/ && git clone -b roc-1.8.x-pr457-altfix https://github.com/deven-amd/HIP.git 
cd /root/HIP && mkdir build && cd build && cmake .. && make package -j$(nproc) && dpkg -i *.deb

version=0.15.0
cd /root/
wget https://github.com/bazelbuild/bazel/releases/download/$version/bazel-$version-installer-linux-x86_64.sh
chmod a+x bazel-$version-installer-linux-x86_64.sh
./bazel-$version-installer-linux-x86_64.sh
