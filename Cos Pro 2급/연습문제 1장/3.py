def func_a(month, day):
    # @부분이 빈칸입니다. 3칸만 채우면 되는 문제입니다.
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0;
    # 4월까지를 더하기 위한 for 문
    for i in range(0,month-1):
        total += month_list[i]

    total += day # day 만큼을 더해줌
    total=total
    return total - 1


def solution(start_month, start_day, end_month, end_day):
    start_total = func_a(start_month, start_day) # step 1
    end_total = func_a(end_month, end_day) #  step 2
    return end_total - start_total #  step 2


# The following is code to output testcase.
start_month = 1
start_day = 2
end_month = 2
end_day = 2
ret = solution(start_month, start_day, end_month, end_day)

# Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")