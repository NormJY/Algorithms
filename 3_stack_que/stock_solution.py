# programmers coding test practice:
# 스택/큐 - 주식가격
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def stock_solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i] += 1
    
    return answer