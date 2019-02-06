#version=0.15.0
version=0.19.2
cd /root/
wget https://github.com/bazelbuild/bazel/releases/download/$version/bazel-$version-installer-linux-x86_64.sh
chmod a+x bazel-$version-installer-linux-x86_64.sh
./bazel-$version-installer-linux-x86_64.sh
