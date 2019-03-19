
all_tests="tests(//tensorflow/... except //tensorflow/compiler/... except //tensorflow/contrib/...)"
#echo $all_tests

python_tests="kind(py_*, $all_tests)"
# echo $python_tests

small_medium_tests="attr(size, \"small|medium\", $python_tests)"
# echo $small_medium_tests

gpu_ci_excluded_tests="attr(tags, \"no_oss|oss_serial|no_gpu|benchmark-test\", $small_medium_tests)"
# echo $gpu_ci_excluded_tests

gpu_ci_tests="$small_medium_tests except $gpu_ci_excluded_tests"
# echo $gpu_ci_tests

rocm_ci_excluded_tests="attr(tags, \"no_oss|oss_serial|no_gpu|no_rocm|benchmark-test\", $small_medium_tests)"
# echo $rocm_ci_excluded_tests

rocm_ci_tests="$small_medium_tests except $rocm_ci_excluded_tests"
# echo $rocm_ci_tests


no_gpu_tests="attr(tags, no_gpu, $small_medium_tests)"
no_rocm_tests="attr(tags, no_rocm, $small_medium_tests)"


# echo "all tests :" `bazel query $all_tests | wc -l`

# echo "python tests :" `bazel query $python_tests | wc -l`

# echo "small medium tests :" `bazel query $small_medium_tests | wc -l`

# echo "gpu_ci_excluded tests :" `bazel query $gpu_ci_excluded_tests | wc -l`

# echo "gpu_ci tests :" `bazel query $gpu_ci_tests | wc -l`

# echo "rocm_ci_excluded tests :" `bazel query $rocm_ci_excluded_tests | wc -l`

# echo "rocm_ci tests :" `bazel query $rocm_ci_tests | wc -l`

# echo "no_rocm tests :" `bazel query $no_rocm_tests | wc -l`


bazel query $no_gpu_tests
# bazel query $no_rocm_tests
