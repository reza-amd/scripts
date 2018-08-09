#docker_image=sunway513/hiptensorflow:tf18-rocm181-rc2-v1
#docker_image=rocm/tensorflow:rocm1.8.2-tf1.8-python3-dev
#docker_image=devenamd/tensorflow:tf18_rocm182_base_180727
docker_image=rocm/rocm-terminal:1.8.2
#docker_image=sunway513/hiptensorflow:rocm1.8.2-rc5-tf1.8-v1

container_name=deven_rocm182_base

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
