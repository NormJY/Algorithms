# programmers coding test practice:
# 연습문제 - 짝수와 홀수
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def numx_solution(x, n):
    answer = []
    for i in range(1, n + 1):
        answer.append(x * i)
    return answer


# 원래는 다음과 같은 함수를 작성했었습니다.

# def numx_solution(x, n):
	# answer = list(range(x, x*(n+1), x))
	# return answer

# 그런데 테스트 8번에서 자꾸 런타임 에러가 발생하여, 다른 방법을 찾았습니다.