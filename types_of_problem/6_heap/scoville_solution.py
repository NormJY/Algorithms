# programmers coding test practice:
# 힙(Heap) - 더 맵게
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

# https://liveyourit.tistory.com/191 의 코드를 참고했습니다.

# 파이썬에서는 우선순위 큐 알고리즘의 구현을 제공하는 heapq 모듈을 제공한다.
# heappush: 힙에 값을 push
# heappop: 힙에서 값을 꺼냄
# heapify: 리스트 x를 힙으로 변환시킬 수 있음.
import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    
    while 1:
        if len(scoville) <= 1 and scoville[0] < K:
            count = -1
            break
        if scoville[0] >= K:
            break
        new_scov = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)  # 섞은 음식의 스코빌 지수
        heapq.heappush(scoville, new_scov)
        count += 1
    
    return count