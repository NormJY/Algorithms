# programmers coding test practice:
# 연습문제 - 행렬의 곱셈
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

# 간단한 코드 구현을 위해 파이썬의 수치해석 라이브러리인 numpy를 활용했습니다.

import numpy as np

def matmul_solution(arr1, arr2):
    
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
	
	# 채점 시 넘파이 array가 아닌, 리스트 형식의 행렬을 확인하므로,
	# tolist() 메서드를 활용하여 넘파이 어레이를 리스트로 바꿨습니다. 
    answer = np.dot(arr1, arr2).tolist()
    
    return answer