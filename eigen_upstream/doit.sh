
dir1=/home/deven/deven/projects/fp16_support/Eigen/eigen_archive
#dir1=/home/deven/deven/projects/fp16_support_tf18/Eigen/eigen_archive
#dir1=/home/deven/deven/projects/eigen_upstream/hipeigen

dir2=/home/deven/deven/projects/eigen_upstream/eigen-upstream

#dir1=CUDA
#dir2=HIP/hcc

meld $dir1/$1 $dir2/$1 &
