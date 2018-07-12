#!/home/deven/anaconda3/bin/python3

import os
import subprocess
import filecmp
import shutil

upstream_dir = "/home/deven/deven/projects/eigen_upstream/rocm_fork/eigen-upstream"
official_dir = "/home/deven/deven/projects/eigen_upstream/official_fork/eigen"

changed_files = """
Eigen/Core
Eigen/src/Core/GeneralProduct.h
Eigen/src/Core/GenericPacketMath.h
Eigen/src/Core/MathFunctions.h
Eigen/src/Core/ProductEvaluators.h
Eigen/src/Core/arch/GPU/Half.h
Eigen/src/Core/arch/GPU/PacketMathHalf.h
Eigen/src/Core/arch/GPU/TypeCasting.h
Eigen/src/Core/arch/HIP/hcc/math_constants.h
Eigen/src/Core/functors/AssignmentFunctors.h
Eigen/src/Core/functors/BinaryFunctors.h
Eigen/src/Core/util/Macros.h
Eigen/src/Core/util/Memory.h
Eigen/src/Core/util/Meta.h
Eigen/src/Eigenvalues/SelfAdjointEigenSolver.h
Eigen/src/SVD/BDCSVD.h
cmake/EigenTesting.cmake
test/CMakeLists.txt
test/half_float.cpp
test/hip_basic.cu
test/hip_common.h
test/main.h
unsupported/Eigen/CXX11/Tensor
unsupported/Eigen/CXX11/src/Tensor/TensorContraction.h
unsupported/Eigen/CXX11/src/Tensor/TensorContractionBlocking.h
unsupported/Eigen/CXX11/src/Tensor/TensorContractionGpu.h
unsupported/Eigen/CXX11/src/Tensor/TensorConvolution.h
unsupported/Eigen/CXX11/src/Tensor/TensorDeviceDefault.h
unsupported/Eigen/CXX11/src/Tensor/TensorDeviceGpu.h
unsupported/Eigen/CXX11/src/Tensor/TensorExecutor.h
unsupported/Eigen/CXX11/src/Tensor/TensorForcedEval.h
unsupported/Eigen/CXX11/src/Tensor/TensorGpuHipCudaDefines.h
unsupported/Eigen/CXX11/src/Tensor/TensorGpuHipCudaUndefines.h
unsupported/Eigen/CXX11/src/Tensor/TensorIndexList.h
unsupported/Eigen/CXX11/src/Tensor/TensorIntDiv.h
unsupported/Eigen/CXX11/src/Tensor/TensorMacros.h
unsupported/Eigen/CXX11/src/Tensor/TensorMeta.h
unsupported/Eigen/CXX11/src/Tensor/TensorMorphing.h
unsupported/Eigen/CXX11/src/Tensor/TensorRandom.h
unsupported/Eigen/CXX11/src/Tensor/TensorReduction.h
unsupported/Eigen/CXX11/src/Tensor/TensorReductionGpu.h
unsupported/Eigen/CXX11/src/Tensor/TensorScan.h
unsupported/Eigen/CXX11/src/util/CXX11Meta.h
unsupported/Eigen/CXX11/src/util/EmulateArray.h
unsupported/Eigen/src/SpecialFunctions/SpecialFunctionsImpl.h
unsupported/Eigen/src/SpecialFunctions/arch/CUDA/CudaSpecialFunctions.h
unsupported/test/CMakeLists.txt
unsupported/test/cxx11_tensor_argmax_gpu.cu
unsupported/test/cxx11_tensor_cast_float16_gpu.cu
unsupported/test/cxx11_tensor_complex_cwise_ops_gpu.cu
unsupported/test/cxx11_tensor_complex_gpu.cu
unsupported/test/cxx11_tensor_contract_gpu.cu
unsupported/test/cxx11_tensor_device.cu
unsupported/test/cxx11_tensor_gpu.cu
unsupported/test/cxx11_tensor_of_float16_gpu.cu
unsupported/test/cxx11_tensor_random_gpu.cu
unsupported/test/cxx11_tensor_reduction_gpu.cu
unsupported/test/cxx11_tensor_scan_gpu.cu
"""

for f in changed_files.split() :
    print (f)
    os.system("cp {} {}".format(os.path.join(upstream_dir, f), os.path.join(official_dir, f)))


