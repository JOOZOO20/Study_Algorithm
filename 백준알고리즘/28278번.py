import sys
n=int(input())

list1=[]
top=-1

for i in range(n):
    para=list(map(int,sys.stdin.readline().split()))
    if para[0]==1:
        list1.append(para[1])
        top+=1
    elif para[0]==2:
        if top!=-1:
            print(list1.pop())
            top-=1
        else:
            print(-1)
    elif para[0]==3:
        print(len(list1))
    elif para[0]==4:
        if top!=-1:
            print(0)
        else:
            print(1)
    elif para[0]==5:
        if top!=-1:
            print(list1[top])
        else:
            print(-1)