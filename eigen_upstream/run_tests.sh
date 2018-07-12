cd build

make \
     gpu_basic \
     half_float \
     cxx11_tensor_reduction_gpu \
     cxx11_tensor_argmax_gpu \
     cxx11_tensor_cast_float16_gpu \
     cxx11_tensor_scan_gpu \
     cxx11_tensor_device \
     cxx11_tensor_gpu \
     cxx11_tensor_contract_gpu \
     cxx11_tensor_of_float16_gpu \
     cxx11_tensor_random_gpu


ctest -R gpu_basic
ctest -R half_float
ctest -R special_functions
ctest -R cxx11_tensor_reduction_gpu
ctest -R cxx11_tensor_argmax_gpu
ctest -R cxx11_tensor_cast_float16_gpu
ctest -R cxx11_tensor_scan_gpu
ctest -R cxx11_tensor_device
ctest -R cxx11_tensor_gpu
ctest -R cxx11_tensor_contract_gpu
ctest -R cxx11_tensor_of_float16_gpu
ctest -R cxx11_tensor_random_gpu
