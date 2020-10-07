# programmers coding test practice:
# 연습문제 - 제일 작은 수 제거하기
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def minremove_solution(arr):
    
    arr.remove(min(arr))
    
    if len(arr) == 0:
        arr.append(-1)
    
    answer = arr 
    return answer