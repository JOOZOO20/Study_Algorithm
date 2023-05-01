#10773번
size=int(input())
lst=[]
for i in range(size):
    num=int(input())
    if num==0:
        lst.pop(len(lst)-1)
    else:
        lst.append(num)

print(sum(lst))
