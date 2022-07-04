# #You may use import as below.
# #import math
#
# def solution(shirt_size):
#     #Write code here.
#     answer = []
#     # for i in range(len(shirt_size)):
#         # shirt_size[i]=shirt_size[i].lower()
#         # xs=0;s=0;m=0;l=0;xl=0;xxl=0
#         # if(shirt_size[i]=="xs"):
#         #     xs+=1
#         # elif(shirt_size[i]=='s'):
#         #     s+=1
#         # elif(shirt_size[i]=='m'):
#         #     m+=1
#         # elif(shirt_size[i]=='l'):
#         #     l+=1
#         # elif(shirt_size[i]=='xl'):
#         #     xl+=1
#         # elif(shirt_size[i]=='xxl'):
#         #     xxl+=1
#     answer=[0]*6 #answer=[0,0,0,0,0,0] ; #answer = [ 0 for i in range(6)] #answer = [ 0 for _ in ragne(6)]
#     # answer = [i+5 for i in range(6)] // 표현식이 필요할때는 이렇게 사용!
#
#     for i in shirt_size:
#         if i == 'XS':
#             answer[0]+=1
#         elif i == 'S':
#             answer[1]+=1
#         elif i == 'm':
#             answer[2] += 1
#         elif i == 'l':
#             answer[3] += 1
#         elif i == 'xl':
#             answer[4] += 1
#
#
#
#     return answer
#
# #The following is code to output testcase.
# shirt_size = ["XS", "S", "L", "L", "XL", "S"]
# ret = solution(shirt_size);
#
# #Press Run button to receive output.
# print("Solution: return value of the function is ", ret, " .")


# 선생님 제안 방식
def solution(shirt_size):
    answer=[]
    answer.append(shirt_size.count("XS"))
    answer.append(shirt_size.count("S"))
    answer.append(shirt_size.count("M"))
    answer.append(shirt_size.count("L"))
    answer.append(shirt_size.count("XL"))
    answer.append(shirt_size.count("XXL"))

    return answer

#The following is code to output testcase.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")