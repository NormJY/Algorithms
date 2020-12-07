# programmers coding test practice:
# 연습문제 - 최대공약수와 최소공배수
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

# math 라이브러리에서 최대공약수를 찾아주는 함수인 gcd를 임포트 합니다.
# gcd 함수는 다음번에 직접 짜보도록 하겠습니다.
from math import gcd

def gcd_solution(n, m):
    answer = [gcd(n, m), (n*m)/gcd(n, m)]
    return answer