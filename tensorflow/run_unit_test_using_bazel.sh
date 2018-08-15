
# cat $1 | while read testname
# for i in {1..10}

testname=$1

# do
bazel test  \
      --test_env=HIP_VISIBLE_DEVICES=0 \
      --test_sharding_strategy=disabled \
      --cache_test_results=no \
      --config=opt \
      --config=rocm \
      $testname
# done

      # --test_env=TF_CPP_MIN_VLOG_LEVEL=1 \
      # --test_env=TF_CPP_MIN_LOG_LEVEL=1 \
      # --test_env=HCC_DB=0x48a \
      # --test_env=MIOPEN_ENABLE_LOGGING=1 \
      # --test_env=MIOPEN_ENABLE_LOGGING_CMD=1 \
      # --test_env=HIP_TRACE_API=2 \
