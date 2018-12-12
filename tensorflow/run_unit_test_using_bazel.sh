
testname=$1

cat $1 | while read testname
# for i in {1..10}

do

# echo $testname

bazel test \
      --test_env=HIP_VISIBLE_DEVICES=0 \
      --test_sharding_strategy=disabled \
      --cache_test_results=no \
      --config=opt \
      --config=rocm \
      $testname

done

      # --test_env=TF_CPP_MIN_VLOG_LEVEL=1 \
      # --test_env=TF_CPP_MIN_LOG_LEVEL=1 \
      # --test_env=HCC_DB=0x48a \
      # --test_env=MIOPEN_ENABLE_LOGGING=1 \
      # --test_env=MIOPEN_ENABLE_LOGGING_CMD=1 \
      # --test_env=HIP_TRACE_API=2 \
      # --config=monolithic \
      # --test_env=TF_ROCM_ENABLE_FUSION=1 \

# bazel query buildfiles(deps($testname))
