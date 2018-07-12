#docker_image=sunway513/hiptensorflow:tf13-rocm172-public-v1
docker_image=sunway513/hiptensorflow:tf18-rocm181-rc2-v1
#
container_name=tf18_rocm181_debug_build

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
