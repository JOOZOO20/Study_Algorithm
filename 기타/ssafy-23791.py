T = int(input())

for test_case in range(1, T + 1):
    n=int(input()) # 선발 인원

    # 우선순위 입력
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    player=[0]*n
    acount=0
    bcount=0

    for i in range(n):
        if acount<=bcount:
            acount+=1
            for j in a:
                if player[j-1]:
                    continue
                else:
                    player[j-1]='A'
                    break
        else:
            bcount+=1
            for j in b:
                if player[j-1]:
                    continue
                else:
                    player[j-1]='B'
                    break
    print(''.join(player))