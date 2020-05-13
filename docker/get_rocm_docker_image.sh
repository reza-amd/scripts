# docker_repo=rocm/eigen-test
# tag=rocm-3.3

# docker_repo=rocm/tensorflow
# tag=rocm3.3-tf2.1-dev
# tag=rocm3.3-tf1.15-dev
# tag=rocm3.1-tf2.1-python3
# tag=rocm2.9-tf1.15-dev

docker_repo=rocm/tensorflow-autobuilds
tag=rocm3.3-52a88d2 # 200512

# docker_repo=rocm/tensorflow-private
# tag=hipclang-vdi-04-fix
# tag=hipclang-bkc3-14-tf1.15-hipcc-x
# tag=rocm2.10-tf-rocsparse-test
# tag=rocm2.9-tf2.0-roctracer-v5
# tag=rocm2.9-tf1.15-roctracer-v3
# tag=rocm2.9-tf1.15-roctracer-v2
# tag=rocm2.9-tf1.15-roctracer-v1
# tag=hipclang-bkc2-build40-tf1.15-VDI-source

# docker_repo=devenamd/tensorflow
# tag=compute-rocm-dkms-no-npi-hipclang-2027
# tag=rocm3.3-python3.6-200422
# tag=hcv_1746
# tag=swdev-231360
# tag=fused_batchnorm_bug
# tag=rocm3.1.0-200304
# tag=rocm3.1.0-200305-01
# tag=rocm3.1.0-200305-02
# tag=hipclang-vdi-bkc-2-40
# tag=hipclang-vdi-bkc-2-40
# tag=hipclang-vdi-03

# docker_repo=devenamd/tensorflow
# tag=rocm3.3-200408
# tag=rocm3.0_191220

# docker_repo=devenamd/mlir
# tag=devenamd/mlir:rocm-3.1-200309
# tag=rocm-2.6-latest

# docker_repo=sunway513/hiptensorflow
#

# docker_repo=mlperf_mitest/object_detection_tf1.14
# docker_repo=mlperf_mitest/object_detection_tf1.15
# tag=rocmgpu

# docker_repo=tensorflow/tensorflow
# tag=nightly-py3

docker_image=$docker_repo:$tag
container_name=deven_auto_rocm33_200512_update_upstream_merge_branches

options=""
options="$options -it"
options="$options --network=host"
options="$options --ipc=host"
options="$options --shm-size 16G"
options="$options --group-add video"
options="$options --cap-add=SYS_PTRACE"
options="$options --security-opt seccomp=unconfined"
options="$options -v $HOME/deven/common:/common"

options="$options --device=/dev/kfd"
options="$options --device=/dev/dri"

# options="$options -v /data/imagenet-inception:/imagenet"

docker run $options --name $container_name $docker_image
