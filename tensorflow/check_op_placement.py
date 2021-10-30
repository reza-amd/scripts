import os
import numpy as np
import tensorflow.compat.v1 as tf1
import tensorflow as tf2

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "0"  # get INFO logs
tf1.disable_v2_behavior()
tf1.debugging.set_log_device_placement(True)
tf2.debugging.set_log_device_placement(True)

tf1.config.set_soft_device_placement(False)
tf2.config.set_soft_device_placement(False)

with tf1.device('/gpu:0'):

  ######## placeholder ########
  a = tf1.placeholder("float", [10])  # placeholder
  with tf1.Session(config=tf1.ConfigProto(log_device_placement=True, allow_soft_placement=False)) as sess:
    a_result=sess.run(a, feed_dict={a:np.random.rand(10)})
    print(f"a_result: {a_result}")
  ######## conv2d_backprop_input ########
  input_sizes = [4, 16, 16, 3]  # NHWC
  filter_sizes = [3, 3, 3, 3]
  out_backprop_ph = tf1.placeholder(
                                       dtype=tf1.dtypes.float32,
                                       shape=input_sizes)
  b = tf1.nn.conv2d_backprop_input(input_sizes=input_sizes,
                                   filter=tf1.ones(filter_sizes,
                                                   dtype=tf1.dtypes.float32),
                                   out_backprop=out_backprop_ph,
                                   strides=[1, 1, 1, 1],
                                   padding="SAME",
                                   data_format="NHWC")  # conv2d_backprop_input

  with tf1.Session(config=tf1.ConfigProto(log_device_placement=True, allow_soft_placement=False)) as sess:
    conv2d_backprop_input_result = sess.run(b, feed_dict={out_backprop_ph:np.random.rand(*input_sizes)})
    print (f"conv2d_backprop_input_result:{conv2d_backprop_input_result}")
  ######## conv2d_backprop_input ########
  c = tf1.range(0, 10)
  with tf1.Session(config=tf1.ConfigProto(log_device_placement=True, allow_soft_placement=False)) as sess:
    range_result = sess.run(c)
    print(f"Range result:{range_result}")

  ######## combined_non_max_suppression ########
  # boxes_size = [4, 2, 1, 4]
  # num_classses = 10
  # scores_size = [4, 2, num_classses]
  # boxes_ph = tf1.placeholder(dtype=tf1.dtypes.float32, shape=boxes_size)
  # scores_ph = tf1.placeholder(dtype=tf1.dtypes.float32, shape=scores_size)
  # d = tf1.image.combined_non_max_suppression(
  #     boxes=boxes_ph,
  #     scores=scores_ph,
  #     max_output_size_per_class=tf1.constant(2),
  #     max_total_size=2,
  #     iou_threshold=0.5,
  #     score_threshold=float('-inf'),
  #     pad_per_class=False,
  #     clip_boxes=True,
  #     name=None)

  # with tf1.Session(config=tf1.ConfigProto(log_device_placement=True, allow_soft_placement=False)) as sess:
  #   try:
  #     sess.run(d, feed_dict={boxes_ph:np.random.rand(*boxes_size), scores_ph:np.random.rand(*scores_size)})
  #   except tf1.errors.InvalidArgumentError as e:
  #     print("combined_non_max_suppression is not supported for GPU.")
  #     print(e.message)
  
  ######## ExpandDims ########
  expand_dims_input = tf1.zeros([2,2,2])
  e = tf1.expand_dims(expand_dims_input, axis=0)
  with tf1.Session(config=tf1.ConfigProto(log_device_placement=True, allow_soft_placement=False)) as sess:
    expand_dim_results = sess.run(e)
    print (f"expand_dim_results: {expand_dim_results.shape}")

  ######## Fill ########
  f = tf1.fill([2, 3], 9)
  with tf1.Session(config=tf1.ConfigProto(log_device_placement=True, allow_soft_placement=False)) as sess:
    fill_results = sess.run(f)
    print (f"fill_results: {fill_results}")

  ######## invert_permutation ########
  invert_permutation_input = tf1.constant([3, 4, 0, 2, 1])
  g = tf1.math.invert_permutation(invert_permutation_input)
  with tf1.Session(config=tf1.ConfigProto(log_device_placement=True, allow_soft_placement=False)) as sess:
    invert_permutation_results = sess.run(g)
    print (f"invert_permutation_results: {invert_permutation_results}")

  ######## size ########
  size_input = tf1.constant([3, 4, 0, 2, 1])
  h = tf1.size(size_input)
  with tf1.Session(config=tf1.ConfigProto(log_device_placement=True, allow_soft_placement=False)) as sess:
    size_results = sess.run(h)
    print (f"size_results: {size_results}")
  
  ######## softmax ########
  softmax_input = tf1.constant([-1, 0., 1.])
  i = tf1.nn.softmax(softmax_input)
  with tf1.Session(config=tf1.ConfigProto(log_device_placement=True, allow_soft_placement=False)) as sess:
    softmax_results = sess.run(i)
    print (f"softmax_results: {softmax_results}")

  ######## squeeze ########
  squeeze_input = tf1.zeros([1, 2, 1, 3, 1, 1])
  j = tf1.squeeze(squeeze_input)
  with tf1.Session(config=tf1.ConfigProto(log_device_placement=True, allow_soft_placement=False)) as sess:
    squeeze_results = sess.run(j)
    print (f"squeeze_results: {squeeze_results.shape}")
  
  ######## stop_gradient ########
  stop_gradient_input = tf1.zeros([2, 2])
  k = tf1.stop_gradient(stop_gradient_input)
  with tf1.Session(config=tf1.ConfigProto(log_device_placement=True, allow_soft_placement=False)) as sess:
    stop_gradient_results = sess.run(k)
    print (f"stop_gradient_results: {stop_gradient_results}")

  ######## Where ########
  where_input = tf1.constant([True, False, False, True])
  l = tf1.where(where_input)
  with tf1.Session(config=tf1.ConfigProto(log_device_placement=True, allow_soft_placement=False)) as sess:
    where_results = sess.run(l)
    print (f"where_results: {where_results}")

  ######## depthwise_conv2d_native ########
  depthwise_conv2d_native_input = tf1.zeros([1, 256, 256, 3])
  depthwise_conv2d_native_filter = tf1.zeros([3, 3, 3, 3])
  depthwise_conv2d_native_strides = [1, 1, 1, 1]
  m = tf1.nn.depthwise_conv2d_native(
    input=depthwise_conv2d_native_input,
    filter=depthwise_conv2d_native_filter,
    strides=depthwise_conv2d_native_strides,
    padding="SAME"
  )
  with tf1.Session(config=tf1.ConfigProto(log_device_placement=True, allow_soft_placement=False)) as sess:
    depthwise_conv2d_native_results = sess.run(m)
    print (f"depthwise_conv2d_native_results: {depthwise_conv2d_native_results}")
  
  ######## avg_pool3d ########
  avg_pool3d_input = tf1.zeros([1, 1, 1, 1, 1])
  avg_pool3d_ksize = 1
  avg_pool3d_strides = 1
  n = tf1.nn.avg_pool3d(
    input=avg_pool3d_input,
    ksize=avg_pool3d_ksize,
    strides=avg_pool3d_strides,
    padding="SAME"
  )
  with tf1.Session(config=tf1.ConfigProto(log_device_placement=True, allow_soft_placement=False)) as sess:
    avg_pool3d_results = sess.run(n)
    print (f"avg_pool3d_results: {avg_pool3d_results}")

  ######## conv3d ########
  conv3d_input = tf1.zeros([2, 2, 256, 256, 2])
  conv3d_filters = tf1.zeros([2,2,2,2,2])
  conv3d_strides = [1,1,1,1,1]
  o = tf1.nn.conv3d(
    input=conv3d_input,
    filters=conv3d_filters,
    strides=conv3d_strides,
    padding="SAME"
  )
  with tf1.Session(config=tf1.ConfigProto(log_device_placement=True, allow_soft_placement=False)) as sess:
    conv3d_results = sess.run(o)
    print (f"conv3d_results: {conv3d_results}")

  ######## max_pool3d ########
  max_pool3d_input = tf1.zeros([1, 1, 1, 1, 1])
  max_pool3d_ksize = 1
  max_pool3d_strides = 1
  p = tf1.nn.max_pool3d(
    input=max_pool3d_input,
    ksize=max_pool3d_ksize,
    strides=max_pool3d_strides,
    padding="SAME"
  )
  with tf1.Session(config=tf1.ConfigProto(log_device_placement=True, allow_soft_placement=False)) as sess:
    max_pool3d_results = sess.run(p)
    print (f"max_pool3d_results: {max_pool3d_results}")

print("Done!")