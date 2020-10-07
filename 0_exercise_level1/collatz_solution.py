# programmers coding test practice:
# 연습문제 - 콜라츠 추측
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

# while문을 사용하여 num이 1이 아니라면 작업을 반복하도록 했습니다.
# 주어진 조건에 따라 작성하면 되는 함수이기에 크게 어렵진 않았습니다.
# 마지막에 테스트케이스 3번과 같은 경우의 조건을 추가하는 것으로 코드를 완성했습니다.

def collatz_solution(num):
    answer = 0
    
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num *= 3
            num += 1
        answer += 1
    
    if answer > 500:
        answer = -1
    
    return answer