# programmers coding test practice:
# 연습문제 - 2016년
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

import datetime

# datetime 모듈을 사용하면 복잡한 계산과정이나 윤년을 고려할 필요가 없습니다.
# 물론 datetime 모듈을 이용하지 않고 직접 짜는 것도 방법이긴 합니다만,
# 간결한 방법이 있는 상황에서 굳이 추천하고 싶진 않습니다.

def day_solution(a, b):
    
    dow = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    answer = dow[datetime.datetime(2016, a, b).weekday()]
    
    return answer