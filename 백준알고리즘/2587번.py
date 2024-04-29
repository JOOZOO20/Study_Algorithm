'''
백준 2587번
문제설명: 원소 5개를 입력받고, 평균과 중앙값을 차례대로 구하는 문제
입력: 원소 5개 각 줄마다 하나씩 입력
출력: 평균, 중앙값을 순서대로 한 줄에 한 값씩 출력함.
'''

list1=[0,0,0,0,0]
for i in range(len(list1)):
    list1[i]=int(input())

list1.sort()
print(sum(list1)//5)
print(list1[2])