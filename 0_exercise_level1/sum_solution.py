# programmers coding test practice:
# 연습문제 - 두 정수 사이의 합
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def sum_solution(a, b):
    
    if a < b:
        answer = sum(range(a,b+1))
    elif a > b:
        answer = sum(range(b,a+1))
    else:
        answer = a
    return answer