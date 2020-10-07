# programmers coding test practice:
# 연습문제 - 나누어 떨어지는 숫자 배열
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def divisor_solution(arr, divisor):
    answer = []
    
    for elem in arr:
        if elem % divisor == 0:
            answer.append(elem)
    if len(answer) == 0:
        answer.append(-1)
    
    answer.sort()
    return answer