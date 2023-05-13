#영수증
totalMoney=int(input())
totalNumber=int(input())
for i in range(totalNumber):
    list1=list(map(int,input().split()))
    totalMoney-=(list1[0]*list1[1])
    totalNumber-=1

if totalMoney==0:
    print('Yes')
else:
    print('No')