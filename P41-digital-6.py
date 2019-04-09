# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 21:40:09 2019

@author: hsieh
"""
r,c=5,4
n=int(input('輸入幾倍的 6 > '))
for row in range(5):
    for expand_row in range(n):
        for col in range(4):
            for expand_col in range(n):
                if (row%2==0 or col==0 or (row==3 and col==3)):
                    print('6',end='')
                else:
                    print(' ',end='')
        print()
