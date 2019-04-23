# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:48:39 2019

@author: hsieh
"""

word='春眠不覺曉處處聞啼鳥夜來風雨聲花落知多少'
#h*w  >= 20個字 P147
h=6
w=4
# w=len(word)//h + ( 1 if len(word)%h else 0) 
for i in range(h):
    for j in range(w-1,-1,-1):
        k=j*h+i
        print(word[k]+str(k) if k < len(word) else '    ' ,end=' ')
    print()
print()
        
        


