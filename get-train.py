#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 11:05:18 2019

@author: msf
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from pandas import DataFrame

le = LabelEncoder()
 
df = pd.read_csv("dataset/combinedaug.csv")
df['index']=df.index

df_bert = pd.DataFrame({'guid':le.fit_transform(df['index']),
            'label':le.fit_transform(df['label']),
            'alpha':['a']*df.shape[0],
            'text':df['comment'].replace(r'\n',' ',regex=True)})

df_bert.to_csv('dataset/train.tsv', sep='\t', index=False, header=False)
