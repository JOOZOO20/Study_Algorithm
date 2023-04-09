#정렬-소트인사이드(1427번)

num=input()
list1=[]
a=""
for i in num:
    list1.append(i)
list1.sort(reverse=True)
for i in list1:
    a+=i
print(int(a))
