export MIOPEN_CHECK_NUMERICS=1
export MIOPEN_ENABLE_LOGGING=1

rm -rf /tmp/nmt_model
 
python -m nmt.nmt \
       --src=en --tgt=vi \
       --hparams_path=nmt/standard_hparams/iwslt15_no_dropout.json \
       --vocab_prefix=/tmp/nmt_data/vocab \
       --train_prefix=/tmp/nmt_data/train \
       --dev_prefix=/tmp/nmt_data/tst2012 \
       --test_prefix=/tmp/nmt_data/tst2013 \
       --out_dir=/tmp/nmt_model
