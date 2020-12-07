# programmers coding test practice:
# 2018 KAKAO BLIND RECRUITMENT - [1차]비밀지도
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

# 정규표현식을 사용한 풀이 방법입니다.

# (\d+): 정수(10 이상도 찾아줌)
# ([SDT]): 'SDT'인 문자열
# ([*#]?): '*#'인 문자를 찾는데, ? -> 없을 수도 있음.

# 해 보고 나니 복잡한 문자열을 다루는 데에 있어 정규표현식을 활용하는 것이 편리하다는 것을 알았습니다.
# 내용이 좀 많아서 공부가 필요할 것 같습니다. 

import re

def DartGame2_solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}
    
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    
    for i in range(len(dart)):
        if dart[i][2] == '*' and [i] > 0:
            dart[i-1] *= 2
        
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    
    answer = sum(dart)
    
    return answer 
