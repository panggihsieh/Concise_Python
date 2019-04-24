# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:14:48 2019

@author: hsieh
"""
w=4
h=4
series=[ i for i in range(0,w*h,1)]
print('---')
for i in range(h):
    for j in range(w):
        key=h*j+i
        print('{:>2}'.format(series[key]),end=' ')
    print()
print('---')
for i in range(h):
    for j in range(w-1,-1,-1):
        key=h*j+i
        print('{:>2}'.format(series[key]),end=' ')
    print()
print('---')
        

        
        