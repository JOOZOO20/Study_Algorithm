originNum=[i for i in range(1,31)]
list1=[]
result=[]
for i in range(28):
    a=int(input())
    list1.append(a)
for i in originNum:
    if i not in list1:
        result.append(i)

print(result[0])
print(result[1])
