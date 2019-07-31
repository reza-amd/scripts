BASE=$HOME

cd $BASE

# git clone https://github.com/llvm/llvm-project.git

# git clone https://github.com/tensorflow/mlir llvm-project/llvm/projects/mlir

# git clone -b exp-mlir-rocm-runner https://github.com/whchung/mlir llvm-project/llvm/projects/mlir

# rm -rf llvm-project/build && mkdir llvm-project/build
cd llvm-project/build

# cmake -G Ninja ../llvm -DLLVM_BUILD_EXAMPLES=ON -DLLVM_ENABLE_CXX1Y=Y -DLLVM_TARGETS_TO_BUILD="host;AMDGPU" -DMLIR_ROCM_RUNNER_ENABLED=1

# cmake --build . --target check-mlir

cmake --build . --target mlir-rocm-runner

/home/rocm-user/llvm-project/build/bin/mlir-rocm-runner \
    /home/rocm-user/llvm-project/llvm/projects/mlir/test/mlir-rocm-runner/gpu-to-hsaco.mlir \
    --shared-libs=/home/rocm-user/llvm-project/build/lib/libhip-runtime-wrappers.so
