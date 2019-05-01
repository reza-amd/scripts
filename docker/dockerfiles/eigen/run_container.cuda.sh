docker_image=devenamd/eigen:eigen-upstream-cuda-v1
container_name=eigen-upstream-nightly-cuda-`date +%y%m%d`

nvidia-docker run \
	      --rm \
	      --network=host \
	      --name $container_name \
	      $docker_image \
	      /root/run_tests_nightly.cuda.sh
