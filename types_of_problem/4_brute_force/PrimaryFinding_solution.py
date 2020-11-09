# programmers coding test practice:
# 완전탐색 - 소수 찾기
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

from itertools import permutations
import math

# 특정 수가 소수임을 판단하는 사용자 정의 함수 작성
def isPrimary(n):
    k = math.sqrt(n)
    
    # 입력이 1일 경우 False 반환
    if n < 2:
        return False
    
    # 속도를 줄이기 위해 제곱근까지만 for문을 돌림
    # 이게 되는 게 신기하긴 하다.
    for i in range(2, int(k) +1):
        if n % i == 0:
            return False
    return True


def PrimaryFinding_solution(numbers):
    # 중복을 제거해 주는 set을 활용하기 위해 answer를 빈 list로 선언
    answer = []
    
    for k in range(1, len(numbers) + 1):
        # permutations는 가능한 모든 경우의 수를 찾아준다.
        # 모든 순열을 고려해주는 메서드라고 생각하면 편할 듯.
        # itertools 모듈에 대해서 좀 공부해 볼 필요가 있을 듯 하다.
        # 빠르기도 하고 편리하니까.
        perlist = list(map(''.join, permutations(list(numbers), k)))
        
        # for 문 아래에 for문을 또 추가할 때 중복되는 것을 없애기 위해
        # 아래와 같이 set으로 중복을 제거해 줬다.
        # 이는 작동시간을 크게 단축시켜준다.
        for i in list(set(perlist)):
            # 위에서 만든 isPrimary 함수로 소수를 판단하고,
            # 소수가 맞으면 answer 리스트에 더한다.
            if isPrimary(int(i)):
                answer.append(int(i))
    
    answer = len(set(answer))

    return answer