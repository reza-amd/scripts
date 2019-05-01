image_name=devenamd/eigen:eigen-upstream-cuda-v1
docker build -t $image_name -f Dockerfile.cuda .
