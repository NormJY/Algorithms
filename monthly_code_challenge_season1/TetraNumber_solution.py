# programmers coding test practice:
# 월간 코드 챌린지 시즌1 - 3진법 뒤집기
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

# 삼진수를 표현하게끔 하는 사용자 정의 함수를 추가했습니다.

def numeral_system(number, base):
    NOTATION = '0123456789ABCDEF'
    q, r = divmod(number, base)
    n = NOTATION[r]
    if q:
        num = numeral_system(q, base) + n
    else:
        num = n
    return num
    # if 문부터 return문까지를 한 줄로 표현할 수 있습니다.
    # return numeral_system(q, base) + n if q else n

# test for numeral system function
print(numeral_system(45, 3))
print(numeral_system(125, 3))


def TetraNumber_solution(n):
    
    # string 으로 역순으로 바꿔준 후,
    # 다시 데이터를 int 타입으로 변경하여 앞부분의 0을 제거합니다.
    rev = int(str(numeral_system(n, 3))[::-1])
    answer = int(str(rev), base=3)
    # int(string, base) -> 특정 진법으로 표현된 string의 10진수 변환을 지원합니다. 
    
    return answer 