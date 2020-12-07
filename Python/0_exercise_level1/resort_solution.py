# programmers coding test practice:
# 연습문제 - 정수 내림차순으로 배치하기
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def resort_solution(n):
    
    conv_n = str(n)
    answer = int(''.join(reversed(sorted(conv_n))))
    
    return answer