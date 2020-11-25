# programmers coding test practice:
# 연습문제 - JadenCase 문자열 만들기
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def JadenCase_solution(s):
    s = s.lower()
    L = s.split(" ")
    answer = ''
    for i in L:
        i = i.capitalize()
        answer += i + " "
    
    return answer[:-1]