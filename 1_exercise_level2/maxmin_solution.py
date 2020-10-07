# programmers coding test practice:
# 연습문제 - 최댓값과 최솟값
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def maxmin_solution(s):
    nums = list(map(int, s.split()))
    answer = ' '.join([str(min(nums)), str(max(nums))])
    return answer