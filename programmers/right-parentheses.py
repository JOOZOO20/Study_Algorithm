# 프로그래머스 올바른 괄호

def solution(s):
    c = 0
    
    for i in s:
        if i == '(':
            c += 1
        else:
            c -= 1
        
        
        if c < 0:
            return False
    
    return c == 0
