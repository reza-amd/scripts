# docker_repo=amddcgpuce/tensorflow-rocm410-ubuntu18
# docker_repo=amdih/tensorflow
# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-dkms-no-npi-hipclang
# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-dkms-no-npi-hipclang-tf-manylinux-2014-env
# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-dkms-no-npi-hipclang-tf-manylinux-env
# docker_repo=devenamd/jax
# docker_repo=devenamd/mlir
# docker_repo=devenamd/nhwc
# docker_repo=devenamd/rocm
# docker_repo=devenamd/tensorflow
# docker_repo=devenamd/tfrt
# docker_repo=manylinux2014-rocm-centos7-tf-test
# docker_repo=rocm/eigen-test
# docker_repo=rocm/jax
# docker_repo=rocm/tensorflow
# docker_repo=rocm/tensorflow-autobuilds
# docker_repo=rocm/tensorflow-private
# docker_repo=rocm/tensorflow-testing
# docker_repo=rocmqa/staging-tf-develop-upstream
# docker_repo=rocmqa/staging-tf-upstream

# tag=

# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-dkms-no-npi-hipclang
# tag=7678_ubuntu_py3_tensorflow_develop-upstream-QA-rocm44

# docker_repo=rocm/tensorflow-private
# tag=mlperf_resnet50_convergence_issue_PR1387_LLVMcommit_222b3aa6

# docker_repo=wangyanyao/rocm-rel-4.3
# tag=ubuntu_py3_tensorflow_r2.5_1

# docker_repo=rocm/tensorflow-private
# tag=rocm4.3.1-rc1-v3-tf2.5-dev

docker_repo=rocm/tensorflow-private
tag=rocm4.3-tf2.5-dev

docker_image=$docker_repo:$tag
container_name=deven_06_rocm430_R25_PENG_DOCKER

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
options="$options -v /data/imagenet:/data/imagenet"
# options="$options -v /data/imagenet-inception:/data/imagenet-inception:"

docker run $options --name $container_name $docker_image
