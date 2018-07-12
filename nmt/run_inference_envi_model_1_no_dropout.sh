export MIOPEN_CHECK_NUMERICS=1
export MIOPEN_ENABLE_LOGGING=1

rm -rf /tmp/envi_model_1_inference_out

mkdir /tmp/envi_model_1_inference_out

python -m nmt.nmt \
    --src=en --tgt=vi \
    --ckpt=/tmp/envi_model_1/translate.ckpt \
    --hparams_path=nmt/standard_hparams/iwslt15_no_dropout.json \
    --out_dir=/tmp/envi_model_1_inference_out \
    --vocab_prefix=/tmp/nmt_data/vocab \
    --inference_input_file=/tmp/nmt_data/tst2013.en \
    --inference_output_file=/tmp/envi_model_1_inference_out/output_infer \
    --inference_ref_file=/tmp/nmt_data/tst2013.vi
