def solution(x):
    num=list(map(int,str(x)))
    thenum=sum(num)
    if x%thenum==0:
        return True
    else:
        return False
