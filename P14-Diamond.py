# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:45:13 2019

@author: hsieh
"""
a=0
n=4
def star(n):
    for i in range(n):
        space=n-1-i
        star=1+i*2
        show=' '*space+'*'*star
        print(show)
    for j in range(n):
        space +=1
        star -=2
        show=' '*space+'*'*star
        print(show)
while 1:
    if n==0 : break
    n=int(input('pls input n > '))
    star(n)
    

    
    
    

