Hour,Minute=map(int,input().split(' '))
if Minute<45:
    if Hour==0:
        Hour=23
        Minute+=15
    else:
        Hour-=1
        Minute+=15
else:
        Minute-=45

print(Hour,Minute)
