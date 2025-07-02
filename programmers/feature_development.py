from collections import deque

def solution(progresses, speeds):
    answer = []
    days=deque()
    length=len(speeds)
    
    for i in range(length):
        tmp=100-progresses[i]
        if tmp%speeds[i]==0:
            days.append(tmp//speeds[i])
        else:
            days.append(tmp//speeds[i]+1)
      
    cur=0
    count=0
    first_release=days[cur]
    
    while(cur<length):
        if first_release>=days[cur]:
            count+=1
            cur+=1
        
        else:
            answer.append(count)
            count=0
            first_release=days[cur]
        
    answer.append(count)
    
    
    return answer
