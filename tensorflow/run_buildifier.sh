HOME=/root

# #################################################################################

# rm -rf $HOME/bazel_buildtools
# cd $HOME && git clone https://github.com/bazelbuild/buildtools bazel_buildtools
# cd $HOME/bazel_buildtools && bazel build //buildifier

# #################################################################################


if [ $1 == "--type=build" ] || [ $1 == "--type=bzl" ] ; then
    fullname=`readlink -f $2`
    cd $HOME/bazel_buildtools && bazel run //buildifier -- $1 $fullname
else
    fullname=`readlink -f $1`
    cd $HOME/bazel_buildtools && bazel run //buildifier -- $fullname
fi
