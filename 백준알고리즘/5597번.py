# BOJ_5597번_과제 안 내신 분..?
# 30명 중에 과제를 내지 않은 2명의 번호를 찾는 문제
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
