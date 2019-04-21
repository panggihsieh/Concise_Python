# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:48:39 2019

@author: hsieh
"""

print('\n輸入一個自然數-->轉成2進位...')
while True:
    num=int(input(' >'))
    if num == 0 :
        break
    else:
        digital_width=len(bin(num))-2 #輸入數字的2進位共有幾位
        for k in range(digital_width-1,-1,-1):
            if num  & (1<<k):
                print('1',end='')
            else:
                print('0',end='')
        print()
