image_name=rocm/eigen-test:rocm-2.10.0-gitlab
docker build -t $image_name -f Dockerfile.rocm .
