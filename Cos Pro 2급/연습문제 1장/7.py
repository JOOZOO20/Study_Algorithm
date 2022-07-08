def solution(scores):
    count = 0
    for s in scores:
        if 650 <= s s<800:
            count += 1
    return count

#The following is code to output testcase. The code below is correct and you shall correct solution function.
scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution(scores)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")

# 틀린 부분 찾으라고 하는 지금 같은 유형은, 미리 실행을 해보고 어디가 판별 잘못되었는지 빠르게 다가가기
# 지금은 10이 잘못된거 보니 조건이 잘못된 것을 찾을 수 있고, 그래서 or을 and로 고칠수 있었음.
# 근데 and 안써도 되고 if 650 <= s < 800 이라고 써줘도 됨.