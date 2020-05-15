docker_repo=devenamd/rocm
tag=rocm-3.5-2272-200515

image_name=$docker_repo:$tag

docker build -t $image_name -f Dockerfile . 
