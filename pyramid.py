# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
line=''
height=4
for n in range(height):
    
    for row in range(4):
        print('*'*(12-4*n),end='')
        s1='-'*(4-1-1*row)
        s2=str(row+1)*(1+2*row)
        line=s1+s2+s1+' '
        print(line*(1+n*1))
        
    
        


