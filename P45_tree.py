# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:49:12 2019

@author: hsieh
"""

line=''
row=5


for i in range(row):# 單獨一個三角形
    s1='-'*(row-1-i)
    s2='/'
    s3='*'*(2*i)
    s4='\\'
    line=s1+s2+s3+s4+s1
    print(line)


for i in range(row): #一列由大到小的三角形
    for j in range(3):
        if i < j:
            line='-'*(row*2-j*2)
            print(line,end='')
        else:
            s1='-'*(row-1-i)
            s2='/'
            s3='*'*(2*i-2*j)
            s4='\\'
            line=s1+s2+s3+s4+s1
            print(line,end='')
    print()
    line=''
