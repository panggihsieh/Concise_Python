# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
1. list 元素為3倍數 [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
2. list 加前、後、任何一位置 
"""

test=[x for x in range(1,51,1) if x%5==0]
print('5的倍數->',test)

test +=[999] ; print('加在尾巴',test)
test = [111] + test  ; print('加在開始',test)
insert_pos=5
test[:5:1]+=['第五個位置']
print('加在某處',test)

