num =int(input())

list1=list(input().split())
list2=[]
for i in range(num):
    list2.append(int(list1[i]))

findNum=int(input())

print(list2.count(findNum))