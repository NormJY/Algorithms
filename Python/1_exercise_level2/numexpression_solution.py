# programmers coding test practice:
# 연습문제 - 숫자의 표현
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def numexpression_solution(n):
    answer = 0
    
    for i in range(1, n//2 + 2):
        s = 0
        for j in range(i, n//2+2):
            s += j
            if s == n:
                answer += 1
            elif s > n:
                break
    answer += 1
    return answer