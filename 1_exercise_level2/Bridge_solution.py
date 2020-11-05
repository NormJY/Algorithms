# programmers coding test practice:
# 연습문제 - 다리를 지나는 트럭 
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def Bridge_solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_on = [0] * bridge_length  # 다리를 건너는 트럭
    curr_weight = 0  # 현재 다리에 올라와 있는 무게
    
    while truck_weights:
        answer += 1
        bridge_out = bridge_on.pop(0)  # 다음에 빠질 트럭의 무게
        curr_weight -= bridge_out
        
        if curr_weight + truck_weights[0] > weight:
            bridge_on.append(0)
        else:
            truck = truck_weights.pop(0)
            bridge_on.append(truck)
            curr_weight += truck
    
    while curr_weight > 0:
        answer += 1
        bridge_out = bridge_on.pop(0)
        curr_weight -= bridge_out
            
    return answer