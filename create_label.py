'''
Title           :create_label.py
Description     :This script create txt file to label train and validation data
Author          :Yidi Wang
Date Created    :Nov 16, 2017
usage           :python create_label.py
python_version  :2.7.12
'''
import re
import os
import os.path 
import glob
import time

root_path = '/home/ubuntu/Documents/Caffe-PilotNet/data'
val_path = '/home/ubuntu/Documents/Caffe-PilotNet/val'
train_path = '/home/ubuntu/Documents/Caffe-PilotNet/train'

start = time.time()

train_file = open("train.txt",'w')
val_file = open("val.txt",'w')
dir_list = os.listdir(root_path)
idx = 0


for dir_name in dir_list:
	n = 0
	idx = idx + 1
	child = os.path.join(root_path, dir_name)
	file_list = os.listdir(child)
	for file_name in file_list:
		n = n + 1
		if n % 10 != 0:
			train_file.write(dir_name + '/' + file_name + ' ' + str(idx-1) + '\n')
			source_file = os.path.join(root_path, dir_name, file_name)
			target_file = os.path.join(train_path, dir_name, file_name)
			if os.path.isfile(source_file): 
				open(target_file, "wb").write(open(source_file, "rb").read())
		elif n % 10 == 0:
			source_file = os.path.join(root_path, dir_name, file_name)
			target_file = os.path.join(val_path, file_name)
			val_file.write(file_name + ' ' + str(idx-1) + '\n')
			if os.path.isfile(source_file): 
				open(target_file, "wb").write(open(source_file, "rb").read())
'''
for dir_name in dir_list:
	n = 0
	idx = idx + 1
	child = os.path.join(root_path, dir_name)
	file_list = os.listdir(child)
	for file_name in file_list:
		n = n + 1
		if n % 10 == 0:
	        val_file.write(file_name + ' ' + str(idx-1) + '\n')
'''
train_file.close()
val_file.close()

c = time.time() - start

print('Total time: %0.2f'%(c))	
