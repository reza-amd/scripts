
# cat $1 | while read testname
# for i in {1..10}
# do

testname=$1
# echo $testname

bazel test \
      --test_env=HIP_VISIBLE_DEVICES=0 \
      --test_sharding_strategy=disabled \
      --test_timeout 600,900,2400,7200 \
      --cache_test_results=no \
      --config=opt \
      --config=rocm \
      $testname

# done

      # --test_env=TF_CPP_MIN_VLOG_LEVEL=1 \
      # --test_env=TF_CPP_MIN_LOG_LEVEL=1 \
      # --test_env=HCC_DB=0x48a \
      # --test_env=HIP_TRACE_API=2 \
      # --test_env=MIOPEN_ENABLE_LOGGING=1 \
      # --test_env=MIOPEN_ENABLE_LOGGING_CMD=1 \
      # --config=monolithic \
      # --test_env=TF_ROCM_FUSION_ENABLE=1 \

# bazel query buildfiles(deps($testname))
