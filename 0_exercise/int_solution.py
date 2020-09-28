# programmers coding test practice:
# 연습문제 - 자연수 뒤집어 배열로 만들기
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def int_solution(n):
    arr = list(str(n))
    answer = list(map(int, reversed(arr)))
    return answer