def solution(phone_number):
    length=len(phone_number)
    temp=phone_number[-4:]
    length-=4
    phone=phone_number[:length]
    answer=''
    for i in phone:
        answer+='*'
    
    answer+=temp
    
    return answer
    
