n = int(input())


result=0

time = list(map(int, input().split()))

time.sort()

for i in range(n):
    result+=time[i]*n
    n-=1

print(result)
