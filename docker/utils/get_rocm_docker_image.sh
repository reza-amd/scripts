# docker_repo=rocm/eigen-test
# tag=rocm-3.7.0-200824
# tag=rocm-3.5.0-200804
# tag=rocm-3.3

# docker_repo=rocm/tensorflow
# tag=rocm3.5-tf2.2-ofed4.6-openmpi4.0.0-horovod

docker_repo=rocm/tensorflow-autobuilds
tag=rocm3.7-1ee7a40 # 200826
# tag=rocm3.5-3757f40 # 200807
# tag=rocm3.3-9ca344d # 200618
# tag=rocm3.3-csb-9d468d0 # 200723

# docker_repo=rocm/tensorflow-private
# tag=rocm37rc3_rocmfork
# tag=rocm3.6-rc3-tf2.1-swdev241977-vdi-from-src

# docker_repo=devenamd/tensorflow
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
# tag=2890_ubuntu_py3_tensorflow_r2.1-hipclang
# tag=2226_ubuntu_py3_tensorflow_master-hipclang

docker_image=$docker_repo:$tag
container_name=deven_14_rocm37_rocmfork

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
