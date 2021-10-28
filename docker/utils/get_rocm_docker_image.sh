

# docker_image=rocm/tensorflow-private:mi200_native_miopen_mitigation


# docker_image=$docker_repo:$tag
# docker_image=rocm/tensorflow-private:mi200_bf16_tensorflow_v1_with_bazel_cache
# docker_image=rocm/tensorflow-private:mi200_denorm_v6
# docker_image=sles_tf2.6:latest
# docker_image=devenamd/tensorflow:rocm45rc4-rocmfork-211022
# docker_image=rocm/tensorflow-autobuilds:ubuntu18.04-rocm4.5.0rc4
docker_image=rocm/tensorflow-private:mi200_denorm_native_rocblas_native_miopen_nhwc_only

container_name=deven_17_MI200_DENORM_NATIVE_MITIGATION_HF_GPT2

docker pull $docker_image

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
options="$options -v /data:/data"
# options="$options -v /data/imagenet-inception:/data/imagenet-inception:"

docker run $options --name $container_name $docker_image
