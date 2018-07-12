# /opt/rocm/bin/hipcc \
#     -E \
#     -c /home/deven/deven/projects/eigen_upstream/eigen-upstream/test/hip_basic.cu \
#     -o /home/deven/deven/projects/eigen_upstream/eigen-upstream/build/test/CMakeFiles/hip_basic.dir//./hip_basic_generated_hip_basic.cu.o \
#     -I/home/deven/deven/projects/eigen_upstream/eigen-upstream \
#     -I/home/deven/deven/projects/eigen_upstream/eigen-upstream/build \
#     -I/usr/include \
#     -I/home/deven/deven/projects/eigen_upstream/eigen-upstream/build/test \
#     -I/opt/rocm/hip/include

/opt/rocm/bin/hipcc \
    -Xclang -ast-print -fsyntax-only \
    -c /home/deven/deven/projects/eigen_upstream/eigen-upstream/test/hip_basic.cu \
    -o /home/deven/deven/projects/eigen_upstream/eigen-upstream/build/hip_basic.int.cc \
    -I/home/deven/deven/projects/eigen_upstream/eigen-upstream \
    -I/home/deven/deven/projects/eigen_upstream/eigen-upstream/build \
    -I/usr/include \
    -I/home/deven/deven/projects/eigen_upstream/eigen-upstream/build/test \
    -I/opt/rocm/hip/include

