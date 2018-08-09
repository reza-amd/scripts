rm -rf eigen.patch.new
diff -Naur eigen/eigen-eigen-429aa5254200 eigen_archive > eigen.patch.new.unsorted
/home/deven/deven/common/scripts/tensorflow/eigen/sort_eigen_patch.py eigen.patch eigen.patch.new.unsorted eigen.patch.new
rm -rf eigen.patch.new.unsorted
cp eigen.patch.new /home/deven/deven/dockerx/eigen.patch
