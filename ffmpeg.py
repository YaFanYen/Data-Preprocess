# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:35:54 2020

@author: milk
"""
import os
import subprocess

path = "/home/ed716/Documents/lrs3_train"
data = os.listdir(path)
length = len(data)
print(length)
data_path = []

for i in range(length):
    data_path.append(path + "/" + data[i])

for i in range(length):
    files = os.listdir(data_path[i])
    data_len = len(files)
    for j in range(data_len):
        name = files[j]
        if name[-4:] == ".mp4":
            command = "ffmpeg -i " + data_path[i] + "/" + files[j] + " -ar 8000 " + data_path[i] + "/" + name[:-4] + ".wav"
            #print(command)   
            subprocess.call(command, shell = True)
