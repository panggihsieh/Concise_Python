# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:46:08 2019

@author: hsieh
"""

r,c,n=5,4,3
lines='' #以每列的每點做繪圖判斷
n=int(input('input expand shape-six num. > '))
for row in range(5):
    
    for col in range(4):
            if (col==0 or row%2==0 or (col==3 and row==3)):lines +='*'*n 
            else :lines +=' '*n
    for i in range(n):print(lines)
    lines=''
    