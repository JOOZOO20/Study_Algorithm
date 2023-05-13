# 원래 기본 수는 주어지는 건데,내가 걍 주어지는 수 없이 그것도 랜덤으로 받음.

import random
numberList=[]
max=0
number=0
number2=0
for i in range(9):
    n=random.randint(0,100)
    if max<n:
        max=n
        number=number2
    number2+=1
print(max)
print(number)
