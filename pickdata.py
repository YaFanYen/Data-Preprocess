# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:35:54 2020

@author: milk
"""
import os
import shutil

path = "/home/ed716/Documents/NewSSD/lrw/lipread_mp4"
savepath="/home/ed716/Documents/NewSSD/DPRNNs/Lipreading/data/data"

data = os.listdir(path)
length = len(data)
data_path = []

for i in range(length):
    data_path.append(path + "/" + data[i])
    #os.mkdir(savepath + "/" + data[i])

files_path = []

for i in range(length):
    files = os.listdir(data_path[i])
    for j in range(len(files)):
        files_path.append(data_path[i] + "/" + files[j])


for i in range(len(files_path)): 
    b = files_path[i]
    a = os.listdir(b)

    for j in range(len(a)):
        if b[-4:] == 'rain':
            shutil.copyfile(b + "/" + a[j] , savepath + "/train/" + a[j])
        elif b[-4:] == '/val':
            shutil.copyfile(b + "/" + a[j] , savepath + "/val/" + a[j])
        elif b[-4:] == 'test':
            shutil.copyfile(b + "/" + a[j] , savepath + "/test/" + a[j])

'''
    for j in range(100):
        name = files[j]
        if name[-4:]==".wav":
            shutil.copyfile(data_path[i] + "/" + name , savepath + "/" + data[i] + "/" + name)

files = os.listdir(path)
for i in range(100):
    shutil.copyfile(path + "/" + files[i] , savepath + "/" + files[i])
'''