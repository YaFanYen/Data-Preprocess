# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 16:11:26 2020

@author: milk
"""
import os
import os.path
import shutil

path = "/home/ed716/Documents/NewSSD/TAC-master/data/output/MC_Libri_adhoc/train/3mic"
savepath = "/home/ed716/Documents/NewSSD/Librimix/3_speaker"

data = os.listdir(path)
data_len = len(data)
data_path = []

for i in range(data_len):
    data_path.append(path + "/" + data[i])

for i in range(data_len):
    files = os.listdir(data_path[i])
    files_len = len(files)
    for j in range(files_len):
        name = files[j]
        if name[:-4] == "mixture_mic1":
            shutil.copyfile(data_path[i] + "/" + name, savepath + "/tr/mix/" + data[i] + "_" + name)
        elif name[:-4] == "spk1_mic1":
            shutil.copyfile(data_path[i] + "/" + name, savepath + "/tr/s1/" + data[i] + "_" + name)
        elif name[:-4] == "spk2_mic1":
            shutil.copyfile(data_path[i] + "/" + name, savepath + "/tr/s2/" + data[i] + "_" + name)
