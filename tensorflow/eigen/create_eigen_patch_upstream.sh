rm -rf eigen.patch.new
diff -Naur eigen-base eigen-upstream > eigen.patch.new.unsorted
/home/deven/deven/common/scripts/tensorflow/eigen/sort_eigen_patch.py eigen_fix_rocm_compilation.patch eigen.patch.new.unsorted eigen.patch.new
rm -rf eigen.patch.new.unsorted
