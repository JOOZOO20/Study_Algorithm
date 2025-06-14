def solution(absolutes, signs):
    answer=0
    for i in range(len(signs)):
        if signs[i]:
            print(absolutes[i])
            answer+=absolutes[i]
        else:
            print(-absolutes[i])
            answer+=-absolutes[i]
    return answer
