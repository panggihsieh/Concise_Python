# -*- coding: utf-8 -*-
"""

編班抽籤

"""
import random
ttl_person=50 #全校人數
balls=list(range(1,ttl_person,1))
random.shuffle(balls)
print("打散的新生序列->",balls)
man_ttl,perman_take_ball =  4,10 #共4班，每班10人
counter=0
for i in range(man_ttl):
    print('{}-Person :'.format(counter),end=' ' )
    for j in range(perman_take_ball): 
        print(balls[counter],end=' ' )
        counter +=1
    print()
        
    


