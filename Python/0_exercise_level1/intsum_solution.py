# programmers coding test practice:
# 연습문제 - 자릿수 더하기
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def intsum_solution(n):
    
    answer = 0
    
    for num in str(n):
        answer += int(num)

    return answer