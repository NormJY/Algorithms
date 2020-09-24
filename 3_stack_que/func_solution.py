# programmers coding test practice:
# 스택/큐 - 기능개발
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

import math

def func_solution(progresses, speeds):
    answer = []
    days = []
    
    # 개발에 소요되는 기간 구하기(days)
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i])/speeds[i]))
    
    # 개발에 소요되는 기간 비교 및 배포 수 구하기
    for i, d in enumerate(days):
        if i == 0:
            maxi = d
            answer.append(1)
            continue
            
        if d <= maxi:
            answer[-1] += 1
        else:
            maxi = d
            answer.append(1)
    
    return answer