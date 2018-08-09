# cat $1 | while read testname
# do
#     bazel test --test_env=HIP_VISIBLE_DEVICES=0 --test_sharding_strategy=disabled --cache_test_results=no --config=opt --config=rocm $testname
# done

bazel test -s \
      --test_env=HIP_VISIBLE_DEVICES=0 \
      --test_sharding_strategy=disabled \
      --cache_test_results=no \
      --config=opt \
      --config=rocm \
      $1

#      --test_env=HIP_TRACE_API=2 \
#      --test_env=MIOPEN_ENABLE_LOGGIN=1 \
#      --test_env=HCC_DB=0x48a \
#      --test_env=TF_CPP_MIN_VLOG_LEVEL=1 \
#      --test_env=TF_CPP_MIN_LOG_LEVEL=1 \
