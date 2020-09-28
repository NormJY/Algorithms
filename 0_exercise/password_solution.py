# programmers coding test practice:
# 연습문제 - 시저 암호
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.


def password_solution(s, n):
    
    s = list(s)
    
    # 아스키 코드를 반환해 주는 ord() 함수를 사용합니다.
    # 아스키 코드를 다시 특정한 값으로 반환하는 chr() 함수 또한 사용했습니다.
    
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 +ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 +ord('a'))
    answer = ''.join(s)
    return answer