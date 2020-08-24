set -e

apt-get update --allow-insecure-repositories

apt-get install -y --allow-unauthenticated \
	hipblas \
	hipcub \
	miopen-hip \
	miopengemm \
	rccl \
	rocblas \
	rocfft \
	rocm-cmake \
	rocm-dev \
	rocm-gdb \
	rocm-libs \
	rocm-utils \
	rocrand

apt-get install -y --allow-unauthenticated \
	cmake \
	kmod \
	libnuma-dev \
	pciutils

apt-get clean
rm -rf /var/lib/apt/lists/*
