# programmers coding test practice:
# 연습문제 - 같은 숫자는 싫어
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.


def redup_solution(arr):
    
    answer = []
    
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i-1] != arr[i]:
            answer.append(arr[i])
    
    return answer