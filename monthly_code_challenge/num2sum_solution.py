# programmers coding test practice:
# 월간 코드 챌린지 - 두 개 뽑아서 더하기
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

# 개인적으로 명시적이지 못한 숏코딩을 그렇게 좋아하진 않습니다.
# 문제를 풀고 나서 다른 분들의 풀이를 보니, itertools를 이용하여 한 줄로도 끝내긴 하던데
# 역시 제가 생각하기엔 우아하긴 하지만 직관적으로 확 들어오진 않는다고 생각되어서
# 그냥 제가 푼 방식대로 올리도록 하겠습니다.

def num2sum_solution(numbers):
    nums = []
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            nums.append(numbers[i] + numbers[j])
    
    
    # 중복을 제거하기 위해 set을 활용했습니다.
    answer = sorted(list(set(nums)))
    return answer