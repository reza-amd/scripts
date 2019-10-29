
all_tests="tests(//tensorflow/compiler/...)"
#echo $all_tests

excluded_tests="attr(tags, \"no_gpu|benchmark-test|no_oss\", $all_tests)"
# echo $gpu_ci_excluded_tests

ci_tests="$all_tests except $excluded_tests"
# echo $ci_tests

no_rocm_tests="attr(tags, \"no_rocm[^_]\", $ci_tests)"
# echo $no_rocm_tests

rocm_ci_tests="$ci_tests except $no_rocm_tests"
# echo $rocm_ci_tests

echo "--- XLA ---"

# echo "ci tests :" `bazel cquery $ci_tests | wc -l`
# echo "--------"
# echo "no_rocm tests :" `bazel cquery $no_rocm_tests | wc -l`
# echo "--------"
# echo "rocm_ci tests :" `bazel cquery $rocm_ci_tests | wc -l`
# echo "--------"

bazel cquery $no_rocm_tests

# //tensorflow/compiler/mlir/lite/quantization/tests:glob_lit_tests
# //tensorflow/compiler/mlir/lite/tests/debuginfo:glob_lit_tests
# //tensorflow/compiler/mlir/lite/tests/end2end:glob_lit_tests
# //tensorflow/compiler/mlir/lite/tests/flatbuffer2mlir:glob_lit_tests
# //tensorflow/compiler/mlir/lite/tests/mlir2flatbuffer:glob_lit_tests

# //tensorflow/compiler/mlir/tensorflow/tests/graphdef2mlir:glob_lit_tests
# //tensorflow/compiler/mlir/tensorflow/tests/mlir2graphdef:glob_lit_tests
# //tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model:basic.py.test
# //tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model:cyclic_object_graph.py.test
# //tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model:dag_object_graph.py.test
# //tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model:debug_info.py.test
# //tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model:keras.py.test
# //tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model:shapes_for_arguments.py.test
# //tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model:shapes_for_variables.py.test

# //tensorflow/compiler/mlir/tensorflow:compile_mlir_util_test
# //tensorflow/compiler/mlir/tensorflow:convert_tensor_test
# //tensorflow/compiler/mlir/tensorflow:error_util_test

# //tensorflow/compiler/mlir/xla/tests/translate:glob_lit_tests

# //tensorflow/compiler/tests:cholesky_op_test_cpu
# //tensorflow/compiler/tests:cholesky_op_test_gpu
# //tensorflow/compiler/tests:concat_ops_test_cpu
# //tensorflow/compiler/tests:concat_ops_test_gpu
# //tensorflow/compiler/tests:dense_layer_test
# //tensorflow/compiler/tests:dense_layer_test_gpu
# //tensorflow/compiler/tests:depthwise_conv_op_test_cpu
# //tensorflow/compiler/tests:depthwise_conv_op_test_gpu
# //tensorflow/compiler/tests:fft_test_cpu
# //tensorflow/compiler/tests:fft_test_gpu
# //tensorflow/compiler/tests:jit_test
# //tensorflow/compiler/tests:jit_test_gpu
# //tensorflow/compiler/tests:lstm_test
# //tensorflow/compiler/tests:lstm_test_gpu
# //tensorflow/compiler/tests:matrix_triangular_solve_op_test_cpu
# //tensorflow/compiler/tests:matrix_triangular_solve_op_test_gpu
# //tensorflow/compiler/tests:qr_op_test_gpu
# //tensorflow/compiler/tests:svd_op_test_gpu
# //tensorflow/compiler/tests:tensor_array_ops_test_cpu
# //tensorflow/compiler/tests:tensor_array_ops_test_gpu
# //tensorflow/compiler/tests:xla_ops_test_cpu
# //tensorflow/compiler/tests:xla_ops_test_gpu

# //tensorflow/compiler/xla/client/lib:svd_test_cpu
# //tensorflow/compiler/xla/client/lib:svd_test_gpu

# //tensorflow/compiler/xla/service/gpu/tests:gemm_rewrite_test

# //tensorflow/compiler/xla/service/gpu:buffer_comparator_test
# //tensorflow/compiler/xla/service/gpu:cudnn_fused_conv_rewriter_test

# //tensorflow/compiler/xla/service/mlir_gpu/experimental/conv_emitter:conv_emitter_test
# //tensorflow/compiler/xla/service/mlir_gpu/tests:mlir_gpu_lhlo_gen_test

# //tensorflow/compiler/xla/tests:cholesky_test_cpu
# //tensorflow/compiler/xla/tests:cholesky_test_gpu
# //tensorflow/compiler/xla/tests:conditional_test_cpu
# //tensorflow/compiler/xla/tests:conditional_test_gpu
# //tensorflow/compiler/xla/tests:convolution_test_autotune_disabled_gpu
# //tensorflow/compiler/xla/tests:convolution_test_cpu
# //tensorflow/compiler/xla/tests:convolution_test_gpu
# //tensorflow/compiler/xla/tests:convolution_test_gpu_alternative_layout_gpu
# //tensorflow/compiler/xla/tests:reduce_test_cpu
# //tensorflow/compiler/xla/tests:reduce_test_gpu
# //tensorflow/compiler/xla/tests:scalar_computations_test_cpu
# //tensorflow/compiler/xla/tests:scalar_computations_test_gpu
# //tensorflow/compiler/xla/tests:select_and_scatter_test_cpu
# //tensorflow/compiler/xla/tests:select_and_scatter_test_gpu
# //tensorflow/compiler/xla/tests:token_hlo_test_cpu
# //tensorflow/compiler/xla/tests:token_hlo_test_gpu
# //tensorflow/compiler/xla/tests:xla_hlo_profile_test_cpu
# //tensorflow/compiler/xla/tests:xla_hlo_profile_test_gpu

# //tensorflow/compiler/xla:bit_cast_test

# //tensorflow/compiler/xla:refcounting_hash_map_test
# //tensorflow/compiler/xrt/client:xrt_client_test

