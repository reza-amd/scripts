# docker_repo=rocm/eigen-test
# tag=rocm-4.0.1-210217

# docker_repo=rocm/tensorflow
# tag=

docker_repo=rocm/tensorflow-autobuilds
tag=rocm4.0.1-csb-latest
tag=rocm4.0.1-latest

# docker_repo=rocm/tensorflow-private
# tag=

# docker_repo=devenamd/tensorflow
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
# tag=

# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-dkms-no-npi-hipclang
# tag=

# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-dkms-no-npi-hipclang-tf-manylinux-env
# tag=

# docker_repo=manylinux2014-rocm-centos7-tf-test
# tag=

docker_image=$docker_repo:$tag
container_name=deven_21_rocm41rc3_rocmfork_QArocm41

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
