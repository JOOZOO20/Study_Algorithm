# BOJ_2480번_주사위 세개
# 3개의 주사위 중 일치하는 눈의 갯수의 따라 상금을 달리 제공하는 문제
a,b,c=map(int,input().split())

if a==b==c:
    print(10000+a*1000)

elif  a==b or b==c or a==c:
    if a==b:
        print(1000+a*100)
    elif b==c:
        print(1000+b*100)
    else:
        print(1000+a*100)

else:
    print(max(a,b,c)*100)