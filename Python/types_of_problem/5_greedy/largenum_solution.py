# programmers coding test practice:
# 탐욕법 - 큰 수 만들기
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

# 탐욕법이 아닌 stack을 이용했습니다.
def largenum_solution(number, k): 
    num = list(number)
    stack = [num[0]] 
    count = 0 
    for i in range(1, len(num)):
        if count == k: 
            stack = stack + num[i:] 
            break 
        stack.append(num[i]) 
        if stack[-1] > stack[-2]: 
            while(len(stack) != 1 and stack[-1] > stack[-2] and count < k):
                stack[-2], stack[-1] = stack[-1], stack[-2] 
                stack.pop() 
                count += 1 
    return "".join(stack[:len(num)-k])
