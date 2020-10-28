# docker_repo=rocm/eigen-test
# tag=rocm-3.8.0-200923
# tag=rocm-3.7.0-200824
# tag=rocm-3.5.0-200804
# tag=rocm-3.3

# docker_repo=rocm/tensorflow
# tag=rocm3.5-tf2.2-ofed4.6-openmpi4.0.0-horovod

# docker_repo=rocm/tensorflow-autobuilds
# tag=rocm3.8-44e82ea

# docker_repo=rocm/tensorflow-autobuilds
# tag=rocm3.7-csb-652291e

# docker_repo=rocm/tensorflow-private
# tag=rocm3.7-tf2.3-mi100-perf-develop
# tag=rocm3.9-rc3-tf2.3-dev
# tag=rocm3.7-tf2.3-miopen-rn50-0910
# tag=rocm37rc3_rocmfork
# tag=rocm3.6-rc3-tf2.1-swdev241977-vdi-from-src

docker_repo=devenamd/tensorflow
tag=rocm310rc1-tf-rocmfork-201027
# tag=rocm39-tf-rocmfork-r23-rocm-enhanced-pre-rocm-201023
# tag=rocm39-tf-rocmfork-r23-rocm-enhanced-201023
# tag=rocm39rc3-tf-upstream_r21-201023
#tag=rocm39rc3-tf-rocmfork-201022
# tag=rocm39rc2-tf-rocmfork-201014
# tag=rocm39rc_b7-tf-upstream_r21-201012
# tag=rocm39rc_b7-tf-rocmfork-201008
# tag=rocm39rc1-tf-rocmfork-201004
# tag=rocm37-tf-upstream-200928
# tag=rocm39_3805-tf-rocmfork-200923
# tag=rocm39_3805-tf-rocmfork-200921
# tag=rocm38rc3-tf-rocmfork-200921
# tag=rocm38rc3-tf-upstream-200918
# tag=rocm38rc3-tf-upstream-r21-200918
# tag=rocm38rc1-tf-upstream-r21-200912
# tag=rocm38rc1-tf-rocmfork-200907
# tag=rocm37-tf-upstream-r21-200828
# tag=rocm37-tf-upstream-200826
# tag=rocm37rc3-tf-rocmfork-200818
# tag=rocm37rc2-ub1804-tf-upstream-r21-200813
# tag=rocm37rc2-ub1804-tf-upstream-r21-200813
# tag=rocm37rc2-tf-rocmfork-200811
# tag=rocm37-tf-rocmfork-r2.3-200817
# tag=rocm38_3493-tf-rocmfork-200813
# tag=rocm37_3289-tf-rocmfork-200729
# tag=rocm37_3165-tf-rocmfork-200716
# tag=rocm37-tf-rocmfork-200806
# tag=rocm37-rocmfork-horovod-200805
# tag=rocm36-tf-zero-size-symbol-bug
# tag=rocm36-tf-rocmfork-200713
# tag=rocm35-tf-rocmfork-200803
# tag=rocm35-rocmfork-horovod-200805
# tag=rocm33-tf-upstream-18.04-200723

# docker_repo=devenamd/rocm
# tag=3.5.0-200804

# docker_repo=devenamd/mlir
# tag=rocm-3.1-200309

# docker_repo=devenamd/tfrt
# tag=rocm-3.7.0-200826

# docker_repo=sunway513/hiptensorflow
# tag=

# docker_repo=tensorflow/tensorflow
# tag=nightly-py3

# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-dkms-no-npi-hipclang
# tag=3873_ubuntu_py3_tensorflow_develop-upstream-QA-rocm39
# tag=3873_ubuntu_py3_tensorflow_r2.1

# docker_repo=rocmqa/staging-tf2.1
# tag=2890_ubuntu_py3_tensorflow_r2.1-hipclang
# tag=2226_ubuntu_py3_tensorflow_master-hipclang
# tag=3.8-py3-ub18.04-3.8.20366-cc4fd405-hipvdi-stg-build-job567

# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-dkms-no-npi-hipclang-tf-manylinux-env
# tag=3873_ub18.04_tf_1.15

# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-rel-3.9
# tag=3_ubuntu_py3_tensorflow_develop-upstream-QA-rocm39

# docker_repo=compute-artifactory.amd.com:5000/rocm-plus-docker/framework/compute-rocm-rel-3.8-tf-manylinux-env
# tag=16_centos8_tf_1.15

docker_image=$docker_repo:$tag
container_name=deven_38_rocm310rc1_rocmfork

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
# options="$options -v /data/imagenet-inception:/imagenet"
# options="$options -v /data/imagenet-inception:/data/imagenet-inception:"

docker run $options --name $container_name $docker_image
