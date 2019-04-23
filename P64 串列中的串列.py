# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:49:12 2019

@author: hsieh
遍歷 os.walk --> [ (path1,dir_name1,file_name1),.......]
"""
import os
import sys
print('----Dir----')
for (dirpath,dirname,filename) in os.walk('E:\\Download'):
    for dirnames in dirname:
        print(dirpath +'\\'+ dirnames)
print('----File---')
for (dirpath,dirname,filename) in os.walk('E:\\Download'):
    for file in filename:
        print(dirpath + file)
        
    
        
