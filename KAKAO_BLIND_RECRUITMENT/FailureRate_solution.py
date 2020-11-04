# programmers coding test practice:
# 2019 KAKAO BLIND RECRUITMENT - 실패율
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.


def FailureRate_solution(N, stages):
    
    result = {}
    num = len(stages)
    
    for stage in range(1, N+1):
        if num != 0:
            count = stages.count(stage)
            result[stage] = count / num
            num -= count
            
        else:
            result[stage] = 0
            
    return sorted(result, key=lambda x : result[x], reverse=True)