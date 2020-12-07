# programmers coding test practice:
# 연습문제 - 다음 큰 숫자
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def nextnum_solution(n):
    c = bin(n).count('1')
    for i in range(n+1, 1000001):
        if bin(i).count('1') == c:
            return i