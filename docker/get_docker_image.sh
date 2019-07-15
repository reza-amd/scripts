# docker_repo=rocm/eigen-test
docker_repo=rocm/tensorflow
# docker_repo=rocm/tensorflow-autobuilds
# docker_repo=rocm/tensorflow-private
#
# docker_repo=devenamd/tensorflow
#
# docker_repo=sunway513/hiptensorflow


tag=latest

docker_image=$docker_repo:$tag

container_name=deven_rocm26_release_baseline

docker run \
       -it \
       --network=host \
       --device=/dev/kfd \
       --device=/dev/dri \
       --group-add video \
       --cap-add=SYS_PTRACE \
       --security-opt seccomp=unconfined \
       -v $HOME/deven/common:/common \
       -v $HOME/deven/dockerx:/dockerx \
       --name $container_name \
       $docker_image
