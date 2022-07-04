def solution(arr):
    left, right = 0, len(arr)-1
    while left<right:   #range(left,right): 도 가능하답니다!!
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# 5번 문제에서 while의 조건을 left<right가 아닌 range(left,right)로 했는데, 이렇게 해도 감점은 없는 건지 궁금합니다..!

#The following is code to output testcase.
arr = [1, 4, 2, 3]
ret = solution(arr)

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")