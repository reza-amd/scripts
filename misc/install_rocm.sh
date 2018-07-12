# 1. Install kernel 4.13 and reboot:

#sudo apt update && \
#    sudo apt install \
#	 linux-headers-4.13.0-32-generic \
#	 linux-image-4.13.0-32-generic \
#	 linux-image-extra-4.13.0-32-generic \
#	 linux-signed-image-4.13.0-32-generic

#sudo reboot

# 2. Reboot and enter kernel 4.13, check current running kernel version by "uname -r", expect to see:
# 4.13.0-32-generic

# 3. Install ROCm package from internal artifactory:
#sudo sh -c 'echo "deb [arch=amd64] http://172.27.226.104/artifactory/list/rocm-dkms-release-1.7-ubuntu xenial main" > /etc/apt/sources.list.d/rocm.list'
#
#sudo apt-get --allow-unauthenticated update && \
#    sudo apt-get --allow-unauthenticated install -y \
#	 rocm-dkms \
#	 rocm-dev \
#	 hsa-ext-rocr-dev \
#	 hsakmt-roct-dev \
#	 hsa-rocr-dev \
#	 rocm-opencl \
#	 rocm-opencl-dev \
#	 rocm-utils \
#	 rock-dkms \
#	 compute-firmware \
#	 rocm-profiler \
#	 cxlactivitylogger \
#	 miopen-hip \
#	 miopengemm \
#	 rocblas \
#	 hipblas \
#	 rocrand

# 4. Add user to the video group, update ramfs limit on the generic Linux kernel and reboot:

#sudo adduser $LOGNAME video
#sudo sh -c 'echo "vm.max_map_count = 250000" > /etc/sysctl.d/mmap.conf'
#sudo reboot

# 5. Reboot and check if the KFD module is loaded to the system, verify the version ROCK-DKMS and firmware:
# lsmod | grep kfd
# Expect to see:
# amdkfd                266240  4
# amd_iommu_v2           20480  1 amdkfd
# amdkcl                 24576  3 amdttm,amdgpu,amdkfd

# apt --installed list | grep -E 'rock|compute-firmware'
# Expect to see:
#compute-firmware/now 1.7.17 all [installed,local]
#rock-dkms/now 1.7.131-ubuntu all [installed,local]

# 6. Install hipCaffe depended packages (Optional if hipCaffe is not desired)
sudo apt-get --allow-unauthenticated update &&
    sudo apt-get --allow-unauthenticated install -y \
	 pkg-config \
	 protobuf-compiler \
	 libprotobuf-dev \
	 libleveldb-dev \
	 libsnappy-dev \
	 libhdf5-serial-dev \
	 libatlas-base-dev \
	 libboost-all-dev \
	 libgflags-dev \
	 libgoogle-glog-dev \
	 liblmdb-dev \
	 python-numpy python-scipy python3-dev python-yaml python-pip \
	 python-skimage python-opencv python-protobuf \
	 libopencv-dev \
	 libfftw3-dev \
	 libelf-dev \
	 g++-multilib \
	 libunwind-dev \
	 git \
	 libnuma-dev \
	 cmake cmake-curses-gui \
	 vim \
	 emacs-nox \
	 curl \
	 wget \
	 rpm \
	 unzip \
	 bc \
	 dkms

# 7. Clone hipCaffe dependancies and build:
# cd ~ && git clone -b hip https://github.com/ROCmSoftwarePlatform/hipCaffe.git
# cd ~/hipCaffe && cp ./Makefile.config.example ./Makefile.config && make -j$(nproc)
