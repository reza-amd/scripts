image_name=rocm/eigen-test:rocm-2.8-gitlab
docker build -t $image_name -f Dockerfile.rocm .
