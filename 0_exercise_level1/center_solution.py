# programmers coding test practice:
# 연습문제 - 가운데 글자 가져오기
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.



def center_solution(s):
    answer = ''
    idx = len(s)//2
    
    if len(s) % 2 != 0:
        answer = s[idx]
    else:
        answer = s[idx-1:idx+1]
    return answer