# 25305번_BOJ_상 받는 커트라인 점수 구하기

num=list(map(int,input().split(" ")))
scores=list(map(int,input().split(' ')))
scores.sort(reverse=True)
print(scores[num[1]-1])