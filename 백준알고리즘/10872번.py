# BOJ_10872번_팩토리얼
# 기본적인 재귀알고리즘인 팩토리얼을 푸는 문제
def fac(n):
    if n==0 or n==1:
        return 1
    else: 
        return n*fac(n-1)

num=int(input())
print(fac(num))
