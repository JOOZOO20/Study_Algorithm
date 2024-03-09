# BOJ_10828번 스택

num = int(input())

list1=[]

def isEmpty():
    if len(list1)==0:
        return 1
    else:
        return 0


for i in range(num):
    act=input()
    if act=="push":
        list1.append(i)
    elif act=="pop":
        n=isEmpty()
        print("n을 출력: ",n)
        if n==1:
            print(-1)
        else:
            print(list1.pop())
    elif act=="size":
        print(len(list1))
    elif act=="empty":
        print(isEmpty())
    elif act=="top":
        n=isEmpty()
        if n==1:
            print(-1)
        else:
            print(list1[len(list1)-1])

