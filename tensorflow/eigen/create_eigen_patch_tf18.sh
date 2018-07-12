rm -rf eigen.patch.new
diff -Naur eigen-eigen-6913f0cf7d06 eigen_archive > eigen.patch.new.unsorted
/home/deven/deven/common/scripts/tensorflow/eigen/sort_eigen_patch.py eigen_fix_rocm_compilation.patch eigen.patch.new.unsorted eigen.patch.new
rm -rf eigen.patch.new.unsorted
cp eigen.patch.new /home/deven/deven/dockerx/eigen_fix_rocm_compilation.patch
