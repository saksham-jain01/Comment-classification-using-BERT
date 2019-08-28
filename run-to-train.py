#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 11:30:32 2019

@author: msf
"""

import os 
os.system("python get-train.py")
os.system("python bert/run_classifier.py --task_name=cola --do_train=true --do_eval=false --do_predict=false --data_dir=./dataset/ --vocab_file=./cased_L-12_H-768_A-12/vocab.txt --bert_config_file=./cased_L-12_H-768_A-12/bert_config.json --init_checkpoint=./cased_L-12_H-768_A-12/bert_model.ckpt --max_seq_length=128 --train_batch_size=8 --learning_rate=5e-5 --num_train_epochs=3.0 --output_dir=./bert_output/ --do_lower_case=False")
