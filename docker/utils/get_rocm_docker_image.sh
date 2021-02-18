docker_repo=rocm/eigen-test
tag=rocm-4.0.1-210217

# docker_repo=rocm/tensorflow
# tag=rocm4.0-tf2.3-dev

# docker_repo=rocm/tensorflow-autobuilds
# tag=rocm4.0.0-05d7b55
# tag=rocm4.0.0-csb-287ab90

# docker_repo=rocm/tensorflow-private
# tag=rocm4.0.1-v3-tf2.4-dev
# tag=rocm4.0-tf1.15-ofed4.6-openmpi4.0.0-horovod-vdi-debug

# docker_repo=devenamd/tensorflow
# tag=rocm42_6531-tf-rocmfork-210215
# tag=nhwc-layout-rocm40-210216
# tag=rocm4.0-tf1.15-ofed4.6-openmpi4.0.0-horovod-vdi-debug
# tag=rocm41rc1-tf-rocmfork-210210
# tag=nhwc-layout-rocm40-210201
# tag=rocm401-tf-upstream-210203
# tag=rocm41_6440-tf-rocmfork-r23rocm-210128
# tag=rocm40-tf-upstream-r21-210126
# tag=rocm41_6368-tf-rocmfork-210123
# tag=rocm40-tf-upstream-210126
# tag=rocm401rc_b26-tf-rocmfork-210125
# tag=rocm40-tf-rocmfork-get_pip-test-210125
# tag=rocm41_6368-tf-rocmfork-210118
# tag=

# docker_repo=devenamd/rocm
# tag=

# docker_repo=devenamd/mlir
# tag=

# docker_repo=devenamd/tfrt
# tag=

# docker_repo=devenamd/jax
# tag=

# docker_repo=devenamd/nhwc
# tag=rocm40-210128

# docker_repo=sunway513/hiptensorflow
# tag=

# docker_repo=tensorflow/tensorflow
# tag=
# tag=nightly-py3

# docker_repo=rocmqa/staging-tf2.1
# tag=

# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-rel-3.8-tf-manylinux-env
# tag=

# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-rel-3.9
# tag=

# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-rel-3.10
# tag=11_ubuntu_py3_tensorflow_develop-upstream-QA-rocm39

# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-dkms-no-npi-hipclang
# tag=6443_ubuntu_py3_tensorflow_develop-upstream-QA-rocm41

# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-dkms-no-npi-hipclang-tf-manylinux-env
# tag=

# docker_repo=manylinux2014-rocm-centos7-tf-test
# tag=latest

docker_image=$docker_repo:$tag
container_name=deven_15_rocm401_eigen

options=""
options="$options -it"
options="$options --network=host"
options="$options --ipc=host"
options="$options --shm-size 16G"
options="$options --group-add video"
options="$options --cap-add=SYS_PTRACE"
options="$options --security-opt seccomp=unconfined"

options="$options --device=/dev/kfd"
options="$options --device=/dev/dri"

options="$options -v $HOME/deven/common:/common"
# options="$options -v /data-bert:/data-bert"
options="$options -v /data/imagenet:/imagenet"
# options="$options -v /data/imagenet-inception:/data/imagenet-inception:"

docker run $options --name $container_name $docker_image
