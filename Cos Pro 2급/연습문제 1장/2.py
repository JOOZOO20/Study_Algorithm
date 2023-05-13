# You may use import as below.
# import math

def solution(price, grade):
    # Write code here.
    answer = 0
    sale=0
    if grade=="S":
        sale=price*0.05
        answer=price-sale
        # answer=price-price*0.05
        # answer =price*0.95 // 근데 이렇게 하면 실수 많이 나올듯
    elif grade=='G':
        sale=price*0.1
        answer = price - sale
    else:
        sale=price*0.15
        answer = int(price - sale)
    # answer=int(answer)
    return answer


# The following is code to output testcase. # 셤장가면 여기가 없대용
price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)

# Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")

price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)

# Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")