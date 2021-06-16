# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 16:11:26 2020

@author: milk
"""
import os
import os.path
import subprocess

path = "/home/ed716/Documents/NewSSD/Voxceleb/dev/mp4"

data = os.listdir(path)
data_len = len(data)
data_path = []

for i in range(data_len):
    data_path.append(path + "/" + data[i])
for i in range(data_len):
    data_name = data_path[i]
    name = data_name[-4:]
    if int(name) > 5000: 
        command = 'sudo rm -r ' + data_name
        #print(command)
        subprocess.call(command, shell = True)
