# docker_repo=rocm/eigen-test

# docker_repo=rocm/tensorflow

docker_repo=rocm/tensorflow-autobuilds
tag=rocm4.0.0-05d7b55
# tag=rocm4.0.0-csb-287ab90

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

# docker_repo=sunway513/hiptensorflow
# tag=

# docker_repo=tensorflow/tensorflow
# tag=
# tag=nightly-py3

# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-dkms-no-npi-hipclang
# tag=

# docker_repo=rocmqa/staging-tf2.1
# tag=

# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-dkms-no-npi-hipclang-tf-manylinux-env
# tag=

# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-rel-3.9
# tag=

# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-rel-3.8-tf-manylinux-env
# tag=

# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-rel-3.10
# tag=

# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-dkms-amd-feature-targetid
# tag=

# docker_repo=rocmqa/staging-tf-develop-upstream
# tag=

# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-dkms-no-npi-hipclang
# tag=

docker_image=$docker_repo:$tag
container_name=deven_01_rocm40_rocmfork

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
# options="$options -v /data/imagenet-inception:/imagenet"
# options="$options -v /data/imagenet-inception:/data/imagenet-inception:"

docker run $options --name $container_name $docker_image
