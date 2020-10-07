# programmers coding test practice:
# 완전탐색 - 모의고사
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def practice_solution(answers):
    scores = [0, 0, 0]
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == first[i % len(first)]:
            scores[0] += 1
        if answers[i] == second[i % len(second)]:
            scores[1] += 1
        if answers[i] == third[i % len(third)]:
            scores[2] += 1
    
    
    max_score = max(scores)
    answer = []
    for i in range(3):
        if max_score == scores[i]:
            answer.append(i+1)
    
    return answer