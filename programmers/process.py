from collections import deque

def checkmax(deques, nowmax):
    # 지금 존재하는 우선순위들을 리스트에 집어넣음.
    list1=[]
    for i in deques:
        list1.append(i[0])
    
    # 최대값 산정
    if nowmax not in deques:
        nowmax=max(list1)
        
    return nowmax
    

def solution(priorities, location):
    deque1=deque()
    
    # 1. 우선순위 (priorities, index)
    for a,b in enumerate(priorities):
        deque1.append((b,a))
 
    # 2. 본 코드    
    findnum=False
    idx=0
    count=0
    
    # 2-1. max값 설정.
    nowmax=0
    nowmax=checkmax(deque1,nowmax)

    # 2-2. 핵심로직
    while(findnum==False):
        # 원하는 값 찾았을 때
        if deque1[0][0]==nowmax and deque1[0][1]==location:
            count+=1
            findnum=True
            break
        
        # 최대값이긴한데, 찾는 값은 아닐때
        if deque1[0][0]==nowmax and deque1[0][1]!=location:
            deque1.popleft()
            count+=1
            nowmax=checkmax(deque1,nowmax)
            continue
        
        # 최대값이 아니라서, 맨 뒤에 다시 넣어야할때
        else:
            temp=deque1.popleft()
            deque1.append(temp)
            continue
        
    return count
