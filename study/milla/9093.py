import sys

T=int(input())

for i in range(T):
    s=sys.stdin.readline().split()

    for j in range(len(s)):
        if j==len(s)-1:
            print(s[j][::-1])
        else:
            print(s[j][::-1],end=' ')