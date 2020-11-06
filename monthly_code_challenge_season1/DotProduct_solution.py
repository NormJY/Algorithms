# programmers coding test practice:
# 월간 코드 챌린지 시즌1 - 내적
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

# 내적은 원리만 알면 구현하는 데 크게 어렵지 않습니다.
# 특히 파이썬으로는요.

def DotProduct_solution(a, b):
    answer = 0
    
    for i in range(len(a)):
        answer += a[i] * b[i]
    
    return answer
