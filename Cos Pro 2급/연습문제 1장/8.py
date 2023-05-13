# 팰린드롬 문제 빈출문제임
# 삼육구도 빈출문제임
# 팰린드롬이 나오면 안 읽어봐도 뭔지 알아야함.
# 앞에서 읽으나 뒤에서 읽으나 똑같은게 팰린드롬 문제임.

#팰린드롬 logic, 맨 뒤와 맨 앞을 순서대로 비교, 가우스가 1부터 100까지 더한 것 처럼.

## 암기 암기 암기문제

def solution(sentence):
    str = ''
    for c in sentence:
        # 제거 하지 않고, 추가하는 형태로 원하는 값을 문자에 더해서 원하는 값을 출력하는 logic
        if c != '.' and c != ' ': # or->and 여야 두 개 다 제거하는! 원하는 값을 만들 수 있다.
            str += c
    size = len(str)
    for i in range(size // 2): # 여기도 완전 이해 후 암기, 스샷 찍어놨음!
        if str[i] != str[size - 1 - i]: # 여기 완전 이해후 암기
            return False
    return True


# The following is code to output testcase. The code below is correct and you shall correct solution function.
sentence1 = "never odd or even."
ret1 = solution(sentence1)

# Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")

sentence2 = "palindrome"
ret2 = solution(sentence2)

# Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")