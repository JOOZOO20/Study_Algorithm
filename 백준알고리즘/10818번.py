# BOJ_10818번_최소, 최대
# N개의 정수를 리스트로 입력받고, 최소 최대를 차례로 출력하는 문제
n=int(input())
list1=list(map(int,input().split()))
print(min(list1), max(list1))