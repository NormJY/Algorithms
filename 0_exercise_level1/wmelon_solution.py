# programmers coding test practice:
# 연습문제 - 수박수박수박수박수박수?
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def wmelon_solution(n):
    answer = []
    
    for i in range(n):
        if i % 2 == 0:
            answer.append("수")
        else:
            answer.append("박")
    return ''.join(answer)