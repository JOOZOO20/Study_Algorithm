#2750번_수 정렬하기

num=int(input())
list1=[]
for i in range(num):
    a=int(input())
    list1.append(a)
    
list1.sort()

for i in list1:
    print(i)
