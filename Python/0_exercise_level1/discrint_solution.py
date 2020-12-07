# programmers coding test practice:
# 연습문제 - 정수 제곱근 판별
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

# math 라이브러리의 sqrt 메서드를 이용하여 n의 제곱근 root를 구한 후,
# 만약 root가 integer라면 (root+1)의 제곱을 반환하고,
# 그렇지 않다면 -1을 반환하도록 함수를 작성했습니다.

import math

def discrint_solution(n):
    answer = 0
    root = math.sqrt(n)
    
    if math.sqrt(n).is_integer() == True:
        answer = (root+1) * (root+1)
    else:
        answer = -1
    
    return answer