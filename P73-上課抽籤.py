# -*- coding: utf-8 -*-
"""

上課抽籤提問
全班有12隻動物為學生
"""
import random
lots='鼠、牛、虎、兔、龍、蛇、馬、羊、猴、雞、狗、豬'
lots=lots.split('、') 
lots=list(lots)
for i in range(3):
    for j in range(4) :
        lottery_no=random.choice(range(0,12,1)) # 抽完放回，抽0-11號
        print(lots[lottery_no],end=' ')
    print()
        
   



        
    


