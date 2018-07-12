export MIOPEN_ENABLE_LOGGING=1
export HIP_TRACE_API=0x2

rm -rf output
python train.py --data_file=data/tiny_shakespeare.txt --num_epochs=10 --test
