TF_REPO_LOC=/home/deven/deven/repos/tensorflow-upstream

# DOCKERFILE_PATH=$TF_REPO_LOC/tensorflow/tools/ci_build/Dockerfile.rocm
DOCKERFILE_PATH=$TF_REPO_LOC/tensorflow/tools/ci_build/Dockerfile.rocm-hipclang-vdi

DOCKER_CONTEXT_PATH=$TF_REPO_LOC/tensorflow/tools/ci_build

DOCKER_IMAGE_NAME=devenamd/tensorflow:hipclang-vdi-bkc-2-40

# docker image rm -f $DOCKER_IMAGE_NAME

cd $TF_REPO_LOC && \
    docker build -t $DOCKER_IMAGE_NAME -f $DOCKERFILE_PATH $DOCKER_CONTEXT_PATH
