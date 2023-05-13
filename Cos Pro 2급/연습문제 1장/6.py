def solution(number):
    count = 0
    for i in range(1, number + 1):
        current = i
        temp = count
        while current != 0:
            #  question, (current%10)==3 처럼 괄호를 붙이면 int형을 불러올수 없다면서 오류가 나는데, 파이썬 원래 조건문에 괄호가 안되나용,,,?
            if current%10==3 or current%10==6 or current%10==9 :
                count += 1
                print("pair", end = '')
            current = current // 10
        # 만약 33이 들어와서 갯수를 세는데, 3,6,9가 들어있지 않은 숫자는 그대로 그 수를 출력하는 문장임. temp(지금 숫자)와 count가 같으면(count가 없으면 그 숫자는 박수가 없었다는 거니까!)
        if temp == count:
            print(i, end = '')
        print(" ", end = '')
    print("")
    return count

# 암기
'''
 # 내가 입력한 버전 
n=135
count=0
while n>0:
    last=n%10
    # if last==3 or last==6 or last==9:
        count+=1
    n=n//10
    print(last,n)
print(count)
 # 교수님이 입력한 버전 
 n =13553436
count =0
while n>0:
    last =n%10
    if last==3 or last==6 or last==9:
        count+=1
    n=n//10
    print(last,n)

print(count)

''' # 내가 입력한 버전

#The following is code to output testcase.
number = 40
ret = solution(number)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".") 
