# docker_repo=rocm/eigen-test
# docker_repo=rocm/tensorflow
# docker_repo=rocm/tensorflow-autobuilds
# docker_repo=rocm/tensorflow-private
#
# docker_repo=devenamd/tensorflow
docker_repo=devenamd/ubuntu
#
# docker_repo=sunway513/hiptensorflow


# tag=latest
tag=develop.16.04

docker_image=$docker_repo:$tag

container_name=deven_MLIR

options=""
options="$options -it"
options="$options --network=host"
# options="$options --device=/dev/kfd"
# options="$options --device=/dev/dri"
# options="$options --group-add video"
options="$options --cap-add=SYS_PTRACE"
options="$options --security-opt seccomp=unconfined"
options="$options -v $HOME/deven/common:/common"

docker run $options --name $container_name $docker_image

