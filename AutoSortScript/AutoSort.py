# -*- coding: utf-8 -*-
import os
import shutil

#defining location of target and final directory
initial_directory = "C:\\Users\\Carina\\Downloads";
final_directory = {'images':'C:\\Users\\Carina\\Pictures\\Downloaded Images','pdf':'C:\\Users\\Carina\\Documents\\Downloaded Documents'}

files = os.listdir(initial_directory)
# encoding = 'utf-8'
shifted_images = 0;
shifted_files = 0;

for f in files:
    initial_file = initial_directory + '\\' + f;
    if ('jpeg' in f.lower()) or ('jpg' in f.lower()) or('png' in f.lower()):
        final_file_path = final_directory['images'] + '\\' + f;
        shutil.move(initial_file, final_file_path)
        shifted_images+=1
    elif 'pdf' in f.lower():
        final_file_path = final_directory['pdf'] + '\\' + f;
        shutil.move(initial_file, final_file_path)
        shifted_files+=1

print(shifted_images)
print(shifted_files)

