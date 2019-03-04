options=""

options="$options --config=opt"
options="$options --config=rocm"
# options="$options --config=monolithic"

options="$options --test_sharding_strategy=disabled"
options="$options --test_timeout 600,900,2400,7200"
options="$options --cache_test_results=no"
# options="$options --flaky_test_attempts=5"

options="$options --test_env=HIP_VISIBLE_DEVICES=0"

options="$options --test_env=MIOPEN_ENABLE_LOGGING=1"
# options="$options --test_env=MIOPEN_ENABLE_LOGGING_CMD=1"

# options="$options --test_env=KMDUMPISA=1"
# options="$options --test_env=KMDUMPLLVM=1"

# options="$options --test_env=HCC_DB=0x48a"
# options="$options --test_env=HIP_TRACE_API=2"

# options="$options --test_env=TF_CPP_MIN_LOG_LEVEL=1"
# options="$options --test_env=TF_CPP_MIN_VLOG_LEVEL=3"
# options="$options --test_env=TF_ROCM_FUSION_ENABLE=1"
# options="$options --test_env=XLA_FLAGS=\"--xla_dump_optimized_hlo_proto_to=/common/LOGS/\""

# options="$options --test_env="
# options="$options "
# echo $options

# cat $1 | while read testname
# for i in {1..10}
# do

testname=$1
# echo $testname

bazel test $options $testname

# done


# bazel query buildfiles(deps($testname))

# llvm-objdump -disassemble -mcpu=gfx900 your.hsaco

# bazel run --config=rocm --config=opt //tensorflow/compiler/xla/tools:hlo_proto_to_json -- --input_file=/common/LOGS/Types.4.pb --output_file=/common/LOGS/Types.4.pb.json
