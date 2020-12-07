# programmers coding test practice:
# 탐욕법 - 체육복
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def gymsuit_solution(n, lost, reserve):
    
    answer = 0
    
    # 여벌 체육복을 가져 온 학생이 도난당했을 경우를 고려하여, reseve를 변경
    # 이 때 다른 학생에게 체육복을 빌려주지 못할 뿐, 본인은 체육 수업에 참여할 수 있으므로
    # lost 에서도 제외시킴
    # 중복을 허용하지 않는 set의 기능을 활용하면 좋을 것 같다는 생각...
    
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    
#    for l in lost:
#        if l in reserve:
#            lost.reserve(l)
#            reserve.remove(l)
#        else:
#            continue
#    ^----------------------------- 처음에 중복을 없애주고자 생각했던 방법인데, set을 활용하는 게 더 빠르므로 주석처리.
    
    
    # 앞뒤로 체육복을 빌려줄 수 있는지의 여부를 판단하고, lost_set에서 체육복을 빌린 학생을 제거
    
    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)
    
    answer = n - len(lost_set)
            
    return answer
