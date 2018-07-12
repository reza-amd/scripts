## List Docker CLI commands
docker
docker container --help

## Display Docker version and info
docker --version
docker version
docker info

## Execute Docker image
docker run hello-world

## List Docker images
docker image ls

## List Docker containers (running, all, all in quiet mode)
docker container ls
docker container ls --all
docker container ls -a -q

# files related to docker seem to be stored under /var/lib/docker
sudo ls /var/lib/docker

# Create image using this directory's Dockerfile
docker build -t friendlyhello

# Run "friendlyhello" mapping port 4000 to 80
docker run -p 4000:80 friendlyhello

# Run "friendlyhello" mapping port 4000 to 80 (in detached mode)
docker run -d -p 4000:80 friendlyhello

# Gracefully stop the specified container
docker container stop <hash>

# Force shutdown of the specified container
docker container kill <hash>

# Remove specified container from this machine
docker container rm <hash>

# Remove all containers from this machine
docker container rm $(docker container ls -a -q)

# List all images on this machine
docker image ls -a

# Remove specified image from this machine
docker image rm <image id>

# Remove all images from this machine
docker image rm $(docker image ls -a -q)

# Log in this CLI session using your docker credentials
docker login

# Tag <image> for upload to registry
docker tag <image> username/repository:tag

# Upload tagged image to registry
docker push username/repository:tag

# Run image from a registry
docker run username/repository:tag

# attach a new terminal to an already running container
docker exec -ti <container_id> bash
