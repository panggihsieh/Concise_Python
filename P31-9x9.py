# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:17:48 2019

@author: hsieh
"""
for outer in range(1,6):
    for inner in range(1,6):
        print('{}x{}={}'.format(outer,inner,outer*inner),
              end='\t')
    print()
