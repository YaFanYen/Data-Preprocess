from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import sys
import os
sys.path.append("../lib")

data_path = '/home/ed716/Documents/NewSSD/Cocktail/frames'
data = os.listdir(data_path)

def rm_frames(start_idx,end_idx):
    for i in range(start_idx, end_idx):
        name = data[i]
        if name[-6:] == 'ffmpeg':
            command = 'sudo rm %s/%s' % (data_path, name)
            os.system(command)
    
rm_frames(start_idx=0, end_idx=len(data))
