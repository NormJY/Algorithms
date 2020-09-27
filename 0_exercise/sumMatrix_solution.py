# programmers coding test practice:
# 연습문제 - 행렬의 덧셈
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

# 파이썬에서 행렬 연산을 용이하게 하는 numpy 라이브러리를 사용했습니다.
# 문제의 의도는 그게 아니었을 수도 있겠단 생각을 합니다.

import numpy as np

def sumMatrix_solution(arr1, arr2):
    answer = np.ndarray.tolist(np.array(arr1) + np.array(arr2))
    return answer 