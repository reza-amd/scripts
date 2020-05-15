docker_repo=devenamd/rocm
tag=rocm-3.5-2272-200515

image_name=$docker_repo:$tag

container_name=deven_MLIR

docker run \
       -it \
       --network=host \
       --device=/dev/kfd \
       --device=/dev/dri \
       --group-add video \
       --cap-add=SYS_PTRACE \
       --security-opt seccomp=unconfined \
       -v $HOME/deven/common:/common \
       --name $container_name \
       $image_name
