# programmers coding test practice:
# 연습문제 - 소수 찾기
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.


def primenumlist_solution(n):
    
    num = set(range(2, n+1))
    
    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    
    return len(num)