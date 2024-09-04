n=int(input())

money=[25,10,5,1]
con=[]
result=[[0]*4 for _ in range(n)]

for i in range(n):
    a=int(input())
    con.append(a)

for i in range(n):
    for j in range(4):
        result[i][j]=con[i]//money[j]
        con[i]%=money[j]

for i in range(n):
    for j in range(4):
        print(result[i][j], end=' ')
    print(end='\n')