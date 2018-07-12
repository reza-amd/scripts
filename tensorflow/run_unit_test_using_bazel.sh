cat $1 | while read testname
do
    bazel test --test_sharding_strategy=disabled --cache_test_results=no --config=opt --config=rocm $testname
done

