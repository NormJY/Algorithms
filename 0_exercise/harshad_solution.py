# programmers coding test practice:
# 연습문제 - 하샤드 수
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

# lx는 각 자릿수를 string 형식으로 쪼갠 리스트입니다.
# 이후 map 함수를 이용하여 lx의 모든 요소를 int로 변경하고,
# 이를 다시 리스트 자료형으로 받아 각 요소를 더한 값을 sx라고 정의했습니다.
# 그리고 sx로 나누어떨어지면 True, 아니라면 False를 반환하기 위한 조건문을 걸어 줬습니다.

def harshad_solution(x):
    
    answer = True
    lx = list(str(x))
    sx = sum(list(map(int, lx)))
    
    if x % sx != 0:
        answer = False
    
    return answer