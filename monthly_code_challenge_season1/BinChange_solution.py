# programmers coding test practice:
# 월간 코드 챌린지 시즌1 - 이진 변환 반복하기
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

# 그렇게 어려운 문제는 아니었습니다. 오히려 1단계의 3진수 문제가 더 난감했다고 생각합니다.

def BinChange_solution(s):
    
    
    zero_cnt = 0
    conv_cnt = 0
    
    while s != '1':
        zero_cnt += s.count('0')    # 0의 개수 카운트
        s = s.replace('0', '')
        s = format(len(s), 'b')
        conv_cnt += 1   # 이진 변환 횟수 카운트
    
    return [conv_cnt, zero_cnt]