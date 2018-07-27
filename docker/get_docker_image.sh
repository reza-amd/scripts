#docker_image=sunway513/hiptensorflow:tf18-rocm181-rc2-v1
docker_image=rocm/tensorflow:rocm1.8.2-tf1.8-python3-dev
#
container_name=tf18_rocm182_debug_build

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
