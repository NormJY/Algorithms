# programmers coding test practice:
# Summer/Winter Coding(~2018) - 예산
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def budget_solution(d, budget):
    answer = 0
    d.sort()
    
    for i in d:
        budget = budget - i
        answer += 1
        if budget < 0:
            answer -= 1
            break
        elif budget == 0:
            break
    
    return answer