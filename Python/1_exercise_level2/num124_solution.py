# programmers coding test practice:
# 연습문제 - 124나라의 숫자
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def num124_solution(n):
    answer = ''
    
    while n > 0:
        n, i = divmod(n, 3)
        if i == 0:
            n = n - 1
            
        answer = '412'[i] + answer
        
    return answer