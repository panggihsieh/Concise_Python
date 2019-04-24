# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 09:22:12 2019

@author: hsieh
"""
series=[x for x in range(20)]
#h*w >= 20
h=5
w=4
for i in range(h):
    for j in range(w-1,-1,-1):
        items=h*j+i
        if items < len(series):
            print('{:>2}'.format(series[items]),end=' ')
        else:
            print('{:>2}'.format(' '),end=' ')
    print()
print()






    