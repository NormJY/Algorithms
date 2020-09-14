# programmers coding test practice:
# 정렬 - k번째 수
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.


def kth_solution(array, commands):
    answer = []
    
    # commands에서 순차적으로 [i, j, k] 리스트를 부르고, 이에 대한 작업을 진행합니다.
    # com은 commands 안에 포함된 1차원 리스트입니다.
    for com in commands:
        # commands의 i, j에 따라 매개변수로 받은 array 리스트를 자르고 정렬해줍니다.
        # 정렬한 리스트를 sarray라는 새 리스트에 저장해줍니다.
        sarray = sorted(array[com[0]-1:com[1]])
        
        # 정렬한 리스트에서 k번째 수를 찾고 그를 answer에 저장해줍니다.
        # 인덱스 조정을 위해 com[2]에서 1을 빼줬습니다.
        answer.append(arr[com[2]-1])
    return answer