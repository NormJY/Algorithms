# programmers coding test practice:
# 연습문제 - 약수의 합
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.


def divsum_solution(n):
    
    divisors = []
    
    for i in range(1, n+1):
        if n % (i) == 0:
            divisors.append(i)
    
    answer = sum(divisors)
    
    return answer