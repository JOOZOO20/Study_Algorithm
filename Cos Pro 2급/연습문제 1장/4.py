def func_a(arr):
    counter = [0 for _ in range(1001)]
    # 여기는 원래 빈칸이 아니었지만, 여기 부분을 지우고 외울때까지 암기해야함.
    for x in arr:
        counter[x] += 1 # 데이터 자체를 그대로 인덱스 번호로 사용하는 for 문장
    return counter

def func_b(arr):
    ret = 0
    for x in arr:
        if ret < x:
            ret = x
    return ret

def func_c(arr):
    INF = 1001
    ret = INF
    for x in arr:
        if x != 0 and ret > x: # 이문장 진짜 주의. full coding 했을때 이 문장을 안쓰면 최대/최소 정확히 안나옴
            ret = x
    return ret

def solution(arr):
    # 문제설명에서 제공하는 함수의 단계가 여기 solution함수의 순서와 순서가 동일하다. == this is 꿀팁
    # 빈칸채우기는 변수이름에 hint가 정말 가득함. ex. return 변수명 보고 맞는걸 대입하면 됩니다.
    # 본 출제의도는 함수 내부 body를 보고 변수이름과 함수이름을 선택하라는 거였음.
    counter = func_a(arr) # 1단계

    ## 여기 매개벼수 완전 주의해야해. 어떤 리스트의 최대값을  찾는지 그게 중요함. arr의 최대값을 찾는게 아니라,
    ##counter의 최대값을 찾는게 문제임을 주의하자.

    max_cnt = func_b(counter) # 2단계
    min_cnt = func_c(counter) # 3단계
    return max_cnt // min_cnt # 4단계 # 이부분 암기. 몫을 한방에 int 형으로 구한는거!

# 근데 int 형과 float형 문제에서 제시한대로 쓰지 않으면 감점되는 경우가 있음.

#The following is code to output testcase.
arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution(arr)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")