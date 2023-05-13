# BOJ_2525번_오븐시계
# 현재 시각으로부터 오븐 요리 완료 시각을 안내해주는 문제

hour,min=map(int,input().split())
time=int(input())

#만약 60보다 클 경우_즉, 시간이 추가되는 경우
if time>=60:
    #time을 60으로 나눈 몫(즉, 시간)을 더함
    hour+=time//60
    #만약 기존 분+time을 60으로 나눈 나머지(즉, 분)을 더하면 1시간을 초과하는 경우
    if (min+(time%60))>=60:
        hour+=1
        min+=(time%60)-60
    # 요리하는데 필요한 분(minute)가 1시간을 초과하지 않는 경우
    else:
        min+=time%60
# 요리하는 데 필요한 시간 분(minute)만 추가되는 경우
else:
     #만약 기존 분(minute)+time을 더하면 1시간을 초과하는 경우
    if (min+time)>=60:
        hour+=1
        min+=time-60
    else:
        min+=time
#만약 24시간을 초과할 경우 0으로 초기화함.
if hour>=24:
    hour%=24

print(hour,min)