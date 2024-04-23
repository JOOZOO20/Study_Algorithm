list1=[]

for i in range(10):
    print("값을 입력해 : ",end='')
    a=int(input())
    list1.append(a)

returnlist=[]
for i in list1:
    number=i%42
    if number not in returnlist:
        returnlist.append(number)
    else:
        pass
    
print(len(returnlist))
