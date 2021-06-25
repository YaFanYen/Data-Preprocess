# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:35:54 2020

@author: milk
"""
import os
import shutil

path = "/home/ed716/Documents/NewSSD/Voxceleb/dev/mp4"
savepath="/home/ed716/Documents/NewSSD/Voxceleb/video"

id_data = os.listdir(path)
id_length = len(id_data)
id_path = []

for i in range(id_length):
    id_path.append(path + "/" + id_data[i])
    #os.mkdir(savepath + "/" + data[i])

idfile_path = []

for i in range(id_length):
    idfile = os.listdir(id_path[i])
    for j in range(len(idfile)):
        idfile_path.append(id_path[i] + "/" + idfile[j])


for i in range(len(idfile_path)): 
    b = idfile_path[i]
    a = os.listdir(b)

    for j in range(len(a)):
        name = b[-19:-12] + '_' + b[-11:] + '_' + a[j]
        shutil.copyfile(b + "/" + a[j] , savepath + '/' + name)



'''        
        if b[-4:] == 'rain':
            shutil.copyfile(b + "/" + a[j] , savepath + "/train/" + a[j])
        elif b[-4:] == '/val':
            shutil.copyfile(b + "/" + a[j] , savepath + "/val/" + a[j])
        elif b[-4:] == 'test':
            shutil.copyfile(b + "/" + a[j] , savepath + "/test/" + a[j])


    for j in range(100):
        name = files[j]
        if name[-4:]==".wav":
            shutil.copyfile(data_path[i] + "/" + name , savepath + "/" + data[i] + "/" + name)

files = os.listdir(path)
for i in range(100):
    shutil.copyfile(path + "/" + files[i] , savepath + "/" + files[i])
'''