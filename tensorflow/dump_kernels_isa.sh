cd /root/tensorflow/bazel-tensorflow && \
    exec env - \
    PATH=/opt/rocm/opencl/bin:/opt/rocm/bin:/opt/rocm/hcc/bin:/opt/rocm/hip/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    PYTHON_BIN_PATH=/usr/bin/python \
    PYTHON_LIB_PATH=/usr/local/lib/python2.7/dist-packages \
    ROCM_TOOLKIT_PATH=/opt/rocm \
    TF_NEED_CUDA=0 \
    TF_NEED_OPENCL=0 \
    TF_NEED_ROCM=1 \
    KMDUMPISA=1 \
    external/bazel_tools/tools/cpp/link_dynamic_library.sh no ignored ignored ignored \
    external/local_config_rocm/crosstool/clang/bin/crosstool_wrapper_driver_rocm -shared -o bazel-out/local_linux-opt/bin/tensorflow/python/_pywrap_tensorflow_internal.so \
    -Lbazel-out/local_linux-opt/bin/_solib_local/_U@local_Uconfig_Urocm_S_Srocm_Chiprand___Uexternal_Slocal_Uconfig_Urocm_Srocm_Srocm_Slib \
    -Lbazel-out/local_linux-opt/bin/_solib_local/_U@local_Uconfig_Urocm_S_Srocm_Crocfft___Uexternal_Slocal_Uconfig_Urocm_Srocm_Srocm_Slib \
    -Lbazel-out/local_linux-opt/bin/_solib_local/_U@local_Uconfig_Urocm_S_Srocm_Chipblas___Uexternal_Slocal_Uconfig_Urocm_Srocm_Srocm_Slib \
    -Lbazel-out/local_linux-opt/bin/_solib_local/_U@local_Uconfig_Urocm_S_Srocm_Cmiopen___Uexternal_Slocal_Uconfig_Urocm_Srocm_Srocm_Slib \
    '-Wl,-rpath,$ORIGIN/../../_solib_local/_U@local_Uconfig_Urocm_S_Srocm_Chiprand___Uexternal_Slocal_Uconfig_Urocm_Srocm_Srocm_Slib' \
    '-Wl,-rpath,$ORIGIN/../../_solib_local/_U@local_Uconfig_Urocm_S_Srocm_Crocfft___Uexternal_Slocal_Uconfig_Urocm_Srocm_Srocm_Slib' \
    '-Wl,-rpath,$ORIGIN/../../_solib_local/_U@local_Uconfig_Urocm_S_Srocm_Chipblas___Uexternal_Slocal_Uconfig_Urocm_Srocm_Srocm_Slib' \
    '-Wl,-rpath,$ORIGIN/../../_solib_local/_U@local_Uconfig_Urocm_S_Srocm_Cmiopen___Uexternal_Slocal_Uconfig_Urocm_Srocm_Srocm_Slib' \
    -Wl,--version-script tensorflow/tf_version_script.lds -pthread \
    -Wl,-no-as-needed -B/opt/rocm/hcc/compiler/bin -no-canonical-prefixes -pass-exit-codes \
    '-Wl,--build-id=md5' '-Wl,--hash-style=gnu' \
    -Wl,--gc-sections \
    -Wl,@bazel-out/local_linux-opt/bin/tensorflow/python/_pywrap_tensorflow_internal.so-2.params
