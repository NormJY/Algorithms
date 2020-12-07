# programmers coding test practice:
# 2018 KAKAO BLIND RECRUITMENT - [1차]비밀지도
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def DartGame_solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'*' : 2, '#' : -1}
    
    a = [0, 0, 0]
    flag = -1
    
    for idx, dart in enumerate(dartResult):
        if dart.isdigit():
            flag += 1
            if dart == '0':
                continue
            elif dartResult[idx+1].isdigit():
                a[flag] = int(dart) * 10
                flag -= 1
            else:
                a[flag] = int(dart)
                
        elif dart in 'SDT':
            a[flag] **= bonus[dart]
            
        else:
            if dart == '*':
                a[flag-1] *= 2
            a[flag] *= option[dart]
        
    
    return sum(a)