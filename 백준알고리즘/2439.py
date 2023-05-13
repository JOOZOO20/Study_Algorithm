n=int(input())

for i in range(1,n+1):
    for j in range(n,i,-1):
        print(' ',end='')
    print('*'*i)

'''
#다른 이의 좋은 방법
n=int(input())
for i in range(1,n+1):
    print(' '*(n-i) + '*'*i)
'''
