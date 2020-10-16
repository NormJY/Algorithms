# programmers coding test practice:
# 해시 - 위장
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

from collections import Counter

def camouflage_solution(clothes):
    counter_each_category = Counter([cat for _, cat in clothes])
    all_possible = 1

    for key in counter_each_category:
        all_possible *= (counter_each_category[key] + 1)

    return all_possible - 1