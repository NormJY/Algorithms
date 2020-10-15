# programmers coding test practice:
# 연습문제 - 땅따먹기
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

# 동적계획법으로 풀어야 하는 대표적인 문제라는데, 솔직히 아직 동적계획법으로 문제를 풀 짬바는 되지 못해서
# 다른 분의 풀이를 참고했습니다.

def land_solution(land):

    for row in range(1, len(land)):
        # 밟을 칸 선택하기
        for i in range(4):
            # 밟은 칸 제외한 나머지 칸
            rest = set(range(4)) - {i}
            # 밟은 칸 제외한 나머지 칸들의 최댓값을 다음 row의 인덱스에 저장
            land[row][i] += max([land[row-1][index] for index in rest])
    
    # 마지막 row 에서 얻을 수 있는 점수의 최댓값을 확인
    
    return max(land[-1])