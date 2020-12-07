# programmers coding test practice:
# 연습문제 - 문자열 내 p와 y의 개수
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def pycount_solution(s):
    answer = False
    
    if s.lower().count('p') == s.lower().count('y'):
        answer = True

    return answer