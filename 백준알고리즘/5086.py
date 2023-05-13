# 약수, 배수와 소수 파트_ [5086번, 배수와 약수문제]
while(True):
    lst=list(map(int,input().split()))
    try:
        if (lst[0]%lst[1])==0:
            print('multiple')
        elif(lst[1]%lst[0])==0:
            print('factor')
        elif(lst[1]%lst[0])!=0 and (lst[0]%lst[1])!=0:
            print('neither')
    except:
        break

