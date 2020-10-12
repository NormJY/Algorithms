# programmers coding test practice:
# 연습문제 - N개의 최소공배수
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

from math import gcd

def lcm_solution(arr):
    arr.sort()
    
    for i in range(1, len(arr)):
        arr[i] = arr[i-1] * arr[i] // gcd(arr[i-1], arr[i]) 
    
    answer = arr[i]
    return answer