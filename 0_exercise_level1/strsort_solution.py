# programmers coding test practice:
# 연습문제 - 문자열 내림차순으로 배치하기
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def strsort_solution(s):
    answer = ''.join(sorted(s, reverse=True))
    return answer