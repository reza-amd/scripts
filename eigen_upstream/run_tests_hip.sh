cd build

make \
     hip_basic \
     half_float \
     cxx11_tensor_reduction_hip \
     cxx11_tensor_argmax_hip \
     cxx11_tensor_cast_float16_hip \
     cxx11_tensor_scan_hip \
     cxx11_tensor_device_hip \
     cxx11_tensor_hip \
     cxx11_tensor_contract_hip \
     cxx11_tensor_of_float16_hip \
     cxx11_tensor_random_hip


ctest -R hip_basic
ctest -R half_float
#ctest -R special_functions
ctest -R cxx11_tensor_reduction_hip
ctest -R cxx11_tensor_argmax_hip
ctest -R cxx11_tensor_cast_float16_hip
ctest -R cxx11_tensor_scan_hip
ctest -R cxx11_tensor_device_hip
ctest -R cxx11_tensor_hip
ctest -R cxx11_tensor_contract_hip
ctest -R cxx11_tensor_of_float16_hip
ctest -R cxx11_tensor_random_hip
