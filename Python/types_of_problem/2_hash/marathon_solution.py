# programmers coding test practice:
# 해시 - 완주하지 못한 선수
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.


# 단 한명의 선수만이 완주하지 못했으므로, 이를 이용하여 구합니다.
# 그렇지만, 이 풀이는 해시의 취지에 맞는 풀이가 아님을 감안해야 합니다.


def marathon_solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for idx in range(len(completion)):
        if participant[idx] != completion[idx]:
            return participant[idx]
    # 마지막 원소가 정답인 경우에는 조건문에서 걸리지 않게 되므로, return을 하나 더 추가합니다.
    return participant[len(completion)]