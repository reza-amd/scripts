#!/bin/bash

export HIP_VISIBLE_DEVICES=0
export HSA_ENABLE_SDMA=0


BASEDIR=$HOME

download_tensorflow_models()
{
    cd $HOME
    #git clone https://github.com/tensorflow/models.git
    pushd models
    popd

    export MODELDIR="$BASEDIR/models"
}

download_tensorflow_benchmarks()
{
    cd $HOME/
    #git clone https://github.com/tensorflow/benchmarks.git
    pushd benchmarks
    popd

    export BENCHDIR="$BASEDIR/benchmarks"
}

run_convolutional_quick_test()
{
    cd $MODELDIR
    rm -f out.txt sum.txt
    numtests=10
    for i in $(eval echo "{1..$numtests}")
    do
	python ./tutorials/image/mnist/convolutional.py --self_test > out.txt 2>&1
	tail -n1 out.txt 2>&1 | tee -a sum.txt
    done
    pass_cnt=`grep 'test_error 0.0' sum.txt | wc -l`
    printf "convolutional.py pass count = %d / $numtests\n", $pass_cnt

    # Expected "final" output:
    #  convolutional.py pass count = 10 / 10
}

run_tutorials_image_mnist()
{
    cd $MODELDIR/tutorials/image/mnist
    python ./convolutional.py

    # Expected "final" output:
    #   Step 8500 (epoch 9.89), 7.2 ms
    #   Minibatch loss: 1.609, learning rate: 0.006302
    #   Minibatch error: 0.0%
    #   Validation error: 1.0%
    #   Test error: 0.8%
}

run_tutorials_image_cifar10()
{
    cd $MODELDIR/tutorials/image/cifar10
    python ./cifar10_train.py --max_steps=5000
    python ./cifar10_eval.py --run_once=True

    # Expected "final" output:
    #   2017-10-10 18:24:38.971358: precision @ 1 = 0.775
}

run_resnet_on_cifar10()
{
    cd $MODELDIR/research/resnet

    # Get the data
    curl -o cifar-10-binary.tar.gz https://www.cs.toronto.edu/~kriz/cifar-10-binary.tar.gz
    tar -xzf cifar-10-binary.tar.gz
    ln -s ./cifar-10-batches-bin ./cifar10

    # Run it
    # NOTE:  here we're using the `timeout` command to limit the length of the run (as
    # there doesn't appear to be a flag for this).  So we're really measuring the accuracy
    # given X seconds of run time.
    timeout 480s python ./resnet_main.py --train_data_path=cifar10/data_batch* \
	    --log_root=/tmp/resnet_model \
	    --train_dir=/tmp/resnet_model/train \
	    --dataset='cifar10' \
	    --num_gpus=1

    # Expected "final" output:
    #   INFO:tensorflow:loss = 2.62153, step = 1, precision = 0.0703125
    #   INFO:tensorflow:global_step/sec: 1.53655
    #   INFO:tensorflow:loss = 1.77221, step = 101, precision = 0.359375
    #   INFO:tensorflow:global_step/sec: 1.55515
    #   INFO:tensorflow:loss = 1.50121, step = 201, precision = 0.5625
    #   INFO:tensorflow:global_step/sec: 1.55693
    #   INFO:tensorflow:loss = 1.33547, step = 301, precision = 0.609375
    #   INFO:tensorflow:global_step/sec: 1.55474
    #   INFO:tensorflow:loss = 1.31107, step = 401, precision = 0.578125
    #   INFO:tensorflow:global_step/sec: 1.55877
    #   INFO:tensorflow:loss = 1.16523, step = 501, precision = 0.726562
}

run_imagenet_classify()
{
    #  Details:  https://github.com/ROCmSoftwarePlatform/hiptensorflow/blob/hip-amd-nccl/tensorflow/g3doc/tutorials/image_recognition/index.md
    cd $MODELDIR/tutorials/image/imagenet
    python ./classify_image.py

    # Expected "final" output:
    #   giant panda, panda, panda bear, coon bear, Ailuropoda melanoleuca (score = 0.89107)
    #   indri, indris, Indri indri, Indri brevicaudatus (score = 0.00779)
    #   lesser panda, red panda, panda, bear cat, cat bear, Ailurus fulgens (score = 0.00296)
    #   custard apple (score = 0.00147)
    #   earthstar (score = 0.00117)
}

run_slim_lenet()
{
    cd $MODELDIR/research/slim
    chmod u+x ./scripts/train_lenet_on_mnist.sh
    ./scripts/train_lenet_on_mnist.sh
}

run_slim_cifarnet()
{
    cd $MODELDIR/research/slim
    chmod u+x ./scripts/train_cifarnet_on_cifar10.sh
    ./scripts/train_cifarnet_on_cifar10.sh
}

run_tf_cnn_benchmarks()
{
    cd $BENCHDIR
    MODELS="alexnet googlenet inception3 inception4 lenet overfeat resnet50 resnet152_v2 trivial vgg11"
    rm -f ./tf_cnn_benchmarks_log.txt
    for m in $MODELS
    do
	python scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py --model=$m --num_batches=2500 --print_training_accuracy=True 2>&1 | tee -a tf_cnn_benchmarks_log.txt
    done
    #grep -E "Model:|total images/sec" tf_cnn_benchmarks_log.txt

    # Expected "final" output:
    # (TITAN X results shown below)
    #   AlexNet     @   2500    images/sec: 2495.8 +/- 1.3 (jitter = 45.6)6.1780.0060.029
    #   GoogleNet   @   2500    images/sec: 422.4 +/- 0.2 (jitter = 7.4)3.6470.0310.156
    #   inception3  @   2500images/sec: 123.1 +/- 0.1 (jitter = 1.5)0.4361.0001.000
    #   lenet       @   2550images/sec: 14362.7 +/- 22.4 (jitter = 827.9)3.5000.0310.156
    #   overfeat    @   2500images/sec: 541.1 +/- 0.2 (jitter = 8.9)3.7480.0310.156
    #   resnet50    @   2500images/sec: 190.8 +/- 0.0 (jitter = 0.9)0.9121.0001.000
    #   trivial     @   2500images/sec: 7949.9 +/- 7.3 (jitter = 354.5)6.6740.4060.406
    #   vgg11       @   2500images/sec: 250.6 +/- 0.1 (jitter = 2.0)4.4570.0310.094
}


run_soumith_benchmarks()
{
    #  Details:  https://github.com/soumith/convnet-benchmarks/tree/master/tensorflow
    # Grab the code
    cd $BASEDIR
    git clone https://github.com/soumith/convnet-benchmarks.git
    BDIR=$BASEDIR/convnet-benchmarks/tensorflow
    cd hiptensorflow

    # Run the benchmarks
    rm -f $BDIR/output_*.log
    MODELS="alexnet overfeat vgg googlenet"
    for m in $MODELS
    do
	python $BDIR/benchmark_${m}.py 2>&1 | tee $BDIR/output_${m}.log
    done

    # Get a quick summary
    find $BDIR -name "output*.log" -print -exec grep 'across 100 steps' {} \; -exec echo \;
}

download_tensorflow_models
download_tensorflow_benchmarks

#run_convolutional_quick_test
#run_tutorials_image_mnist
#run_tutorials_image_cifar10
run_resnet_on_cifar10
#run_imagenet_classify
#run_tf_cnn_benchmarks
#run_soumith_benchmarks

#run_slim_lenet
#run_slim_cifarnet
