#정렬-소트인사이드(1427번)

num=input()
list1=[]
result=""
for i in num:
    list1.append(i)
list1.sort(reverse=True)
for i in list1:
    result+=i
print(int(result))
