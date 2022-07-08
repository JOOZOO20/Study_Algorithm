def solution(characters):
    result = ""
    
    ## 오류있음 고쳐봐바
    result += characters[0]
    for i in range(1,len(characters)):
        if characters[i - 1] != characters[i]:
            result += characters[i]
    return result
#-1이라고 하면 맨 뒤로 가게 됨.

#The following is code to output testcase. The code below is correct and you shall correct solution function.
characters = "senteeeencccccceeee"
ret = solution(characters)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")