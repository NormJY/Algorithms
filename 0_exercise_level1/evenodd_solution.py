# programmers coding test practice:
# 연습문제 - 짝수와 홀수
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def evenodd_solution(num):
    answer = "Even"
    if num % 2 == 1:
        answer = "Odd"
    return answer