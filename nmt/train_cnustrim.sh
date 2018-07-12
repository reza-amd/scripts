python train.py \
       --data_file=./cnustrim/data.txt \
       --output_dir=./cnustrim/output \
       --batch_size=8 \
       --dropout=0.0 \
       --embedding_size=0 \
       --hidden_size=512 \
       --input_dropout=0.0 \
       --learning_rate=0.01 \
       --max_grad_norm=5.0 \
       --model=lstm \
       --num_layers=3 \
       --num_unrollings=256
       
