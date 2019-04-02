
all_tests="tests(//tensorflow/... except //tensorflow/compiler/... except //tensorflow/contrib/...)"
#echo $all_tests

python_tests="kind(py_*, $all_tests)"
# echo $python_tests

small_medium_tests="attr(size, \"small|medium\", $python_tests)"
# echo $small_medium_tests

excluded_tests="attr(tags, \"no_oss|oss_serial|benchmark-test\", $small_medium_tests)"
# echo $gpu_ci_excluded_tests

ci_tests="$small_medium_tests except $excluded_tests"
# echo $ci_tests

no_gpu_tests="attr(tags, \"no_gpu[^_]\", $ci_tests)"
# echo $no_gpu_tests

no_cuda_tests="attr(tags, \"no_cuda[^_]\", $ci_tests)"
# echo $no_cdua_tests

no_gpu_no_cuda_tests="attr(tags, \"no_gpu[^_]|no_cuda[^_]\", $ci_tests)"
# echo $no_gpu_no_cuda_tests

cuda_ci_tests="$ci_tests except $no_gpu_no_cuda_tests"
# echo $cuda_ci_tests

no_rocm_tests="attr(tags, \"no_rocm[^_]\", $ci_tests)"
# echo $no_rocm_tests

no_rocm_v2_tests="attr(tags, \"no_rocm_v2[^_]\", $ci_tests)"
# echo $no_rocm_v2_tests

no_gpu_no_rocm_tests="attr(tags, \"no_gpu[^_]|no_rocm[^_]\", $ci_tests)"
# echo $no_gpu_no_rocm_tests

rocm_ci_tests="$ci_tests except $no_gpu_no_rocm_tests"
# echo $rocm_ci_tests

no_gpu_no_rocm_no_rocm_v2_tests="attr(tags, \"no_gpu[^_]|no_rocm[^_]|no_rocm_v2[^_]\", $ci_tests)"
# echo $no_gpu_no_rocm_no_rocm_v2_tests

rocm_v2_ci_tests="$ci_tests except $no_gpu_no_rocm_no_rocm_v2_tests"
# echo $rocm_ci_tests

no_rocm_no_cuda_tests="attr(tags, \"no_rocm[^_]|no_cuda[^_]\", $ci_tests)"
# echo $no_rocm_no_cuda_tests

no_rocm_no_rocm_v2_no_cuda_tests="attr(tags, \"no_rocm[^_]|no_rocm_v2[^_]|no_cuda[^_]\", $ci_tests)"
# echo $no_rocm_no_cuda_tests

echo "--- non XLA ---"

# echo "all tests :" `bazel query $all_tests | wc -l`
# echo "python tests :" `bazel query $python_tests | wc -l`
# echo "small medium tests :" `bazel query $small_medium_tests | wc -l`
# echo "excluded tests :" `bazel query $excluded_tests | wc -l`

# echo "ci tests :" `bazel query $ci_tests | wc -l`
# echo "--------"
# echo "no_gpu tests :" `bazel query $no_gpu_tests | wc -l`
# echo "--------"
# echo "no_rocm tests :" `bazel query $no_rocm_tests | wc -l`
# echo "no_cuda tests :" `bazel query $no_cuda_tests | wc -l`
# echo "no_rocm_v2 tests :" `bazel query $no_rocm_v2_tests | wc -l`
# echo "--------"
# echo "rocm_ci tests :" `bazel query $rocm_ci_tests | wc -l`
# echo "rocm_v2_ci tests :" `bazel query $rocm_v2_ci_tests | wc -l`
# echo "cuda_ci tests :" `bazel query $cuda_ci_tests | wc -l`
# echo "--------"

# echo "no_gpu_no_rocm tests :" `bazel query $no_gpu_no_rocm_tests | wc -l`
# echo "no_gpu_no_cuda tests :" `bazel query $no_gpu_no_cuda_tests | wc -l`
# echo "no_rocm_no_cuda tests :" `bazel query $no_rocm_no_cuda_tests | wc -l`


# bazel query $no_rocm_tests
bazel query $no_rocm_v2_tests
# bazel query $no_cuda_tests
# bazel query $no_rocm_no_cuda_tests
# bazel query $no_rocm_no_rocm_v2_no_cuda_tests



