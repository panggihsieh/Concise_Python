# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:45:13 2019

@author: hsieh
"""
a=0
for j in range(5):
    print('-'*j,end='')
    a=j
    for i in range(5):
        a +=1
        print(a,end='')
    print('-'*(5-1-j))
    
    
    
    
    

