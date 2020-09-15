# programmers coding test practice:
# 정렬 - h-index
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def hindex_solution(citations):
    citations.sort()
    p_num = len(citations)
    
    for i in range(p_num):
        if citations[i] >= p_num - i:
            answer = p_num - i
            return answer
    return 0