# programmers coding test practice:
# 연습문제 - 문자열 다루기 기본
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def basicstring_solution(s):
    answer = False
    
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            answer = True
    
    return answer