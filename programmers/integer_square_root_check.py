def solution(n):
    k=int(n**(0.5))
    if (k**2)==n and k>0:
        return (k+1)**2
    else:
        return -1
