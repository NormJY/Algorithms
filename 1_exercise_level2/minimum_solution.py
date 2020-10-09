# programmers coding test practice:
# 연습문제 - 최솟값 만들기 
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def minimum_solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer = 0
    
    for a, b in zip(A, B):
        answer += a * b

    return answer