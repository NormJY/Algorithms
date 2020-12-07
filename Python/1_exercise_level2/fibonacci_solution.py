# programmers coding test practice:
# 연습문제 - 피보나치 수
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def fibonacci_solution(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a % 1234567
