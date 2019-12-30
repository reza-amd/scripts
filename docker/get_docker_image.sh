# docker_repo=rocm/eigen-test
# tag=rocm-2.10.0-gitlab
# tag=rocm-2.8-gitlab
# tag=rocm-2.8
# tag=rocm-2.6

# docker_repo=rocm/tensorflow
# tag=rocm2.9-tf1.15-dev

# docker_repo=rocm/tensorflow-autobuilds
# tag=rocm2.8-7eb6e3f
# tag=rocm2.8-5516f09
# tag=rocm2.8-c750a36
# tag=rocm2.6-2704edd

docker_repo=rocm/tensorflow-private
tag=rocm2.9-tf2.0-roctracer-v5
# tag=rocm2.10-tf-rocsparse-test
# tag=rocm2.9-tf1.15-roctracer-v1
# docker_repo=devenamd/tensorflow
# tag=fused_batchnorm_bug

 
# docker_repo=devenamd/tensorflow
# tag=rocm3.0_191220

# docker_repo=devenamd/mlir
# tag=rocm-2.6-latest

# docker_repo=sunway513/hiptensorflow
#

docker_image=$docker_repo:$tag

container_name=deven_rocm29_tf_roctracer

options=""
options="$options -it"
options="$options --network=host"
options="$options --ipc=host"
options="$options --shm-size 16G"
options="$options --device=/dev/kfd"
options="$options --device=/dev/dri"
options="$options --group-add video"
options="$options --cap-add=SYS_PTRACE"
options="$options --security-opt seccomp=unconfined"
options="$options -v $HOME/deven/common:/common"
# options="$options -v /data/imagenet-inception:/imagenet"

docker run $options --name $container_name $docker_image
