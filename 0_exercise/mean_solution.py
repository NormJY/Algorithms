# programmers coding test practice:
# 연습문제 - 평균 구하기
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

# 정말 간단한 문제이고, 각종 모듈에서도 구현되어 있는 기능이지만
# 단순히 해당 언어의 기본 라이브러리만을 이용하여 풀라는 문제같아서 그렇게 풀었습니다.

def mean_solution(arr):
    answer = sum(arr) / len(arr)
    return answer