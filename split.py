# -*- coding: utf-8 -*-
"""
Created on Thu May  2 19:48:02 2019

@author: Milk
"""
import math
import random
import os
import os.path
import shutil

path = "/home/ed716/Documents/NewSSD/TAC-master/data/output/MC_Libri_adhoc/train/3mic"
savepath = "/home/ed716/Documents/NewSSD/Librimix/3_speaker"
data = os.listdir(path)
data_len = len(data)
wav = []
for i in range(data_len):
    wav.append(data[i])
random.shuffle(wav)

val_len = math.floor(data_len * 2/9)
test_len = math.floor(data_len * 1/9)

for i in range (data_len):
    if i < test_len :
       shutil.copytree(path + "/" + wav[i] , savepath + "/tt/" + wav[i])
    elif i < (test_len + val_len) and i >= test_len :
       shutil.copytree(path + "/" + wav[i] , savepath + "/cv/" + wav[i])
    elif i >= (test_len + val_len):
       shutil.copytree(path + "/" + wav[i] , savepath + "/tr/" + wav[i])
  
