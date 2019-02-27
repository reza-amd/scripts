
all_tests="tests(//tensorflow/... except //tensorflow/compiler/... except //tensorflow/contrib/...)"
#echo $all_tests

python_tests="kind(py_*, $all_tests)"
# echo $python_tests

no_rocm_tests="attr(tags,no_rocm,$all_tests)"
# echo $no_rocm_tests

# List all tests
# bazel query $all_tests

# List all python tests
# bazel query $python_tests

# List all no_rocm tests
bazel query $no_rocm_tests

