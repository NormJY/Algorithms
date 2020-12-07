# programmers coding test practice:
# 2018 KAKAO BLIND RECRUITMENT - [1차]비밀지도
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def secretmap_solution(n, arr1, arr2):
    
    # 지도 1, 지도 2를 표현하는 list m1, m2 작성
    m1 = list(range(n))
    m2 = list(range(n))
    
    for i in range(len(arr1)):
        # arr1, arr2에서 해당하는 십진수를 이진수로 변환
        a = format(arr1[i], 'b')
        b = format(arr2[i], 'b')
        # 변환한 이진수 string의 길이가 n이 될 때까지
        # 해당 이진수 string 앞에 0을 추가
        while len(a) != n:
            a = '0' + a
        while len(b) != n:
            b = '0' + b
        m1[i] = list(a)
        m2[i] = list(b)
    
    answer = list(range(n))
    
    # 최종 비밀지도 도출
    # 주어진 지도1, 지도2의 겹쳐지는 부분의 정수 합이 0이면 공백,
    # 아닌 경우엔 #을 더함 
    for i in range(n):
        secret = ''
        for j in range(n):
            if int(m1[i][j]) + int(m2[i][j]) == 0:
                secret = secret + ' '
            else:
                secret = secret + '#'
        answer[i] = secret 

    
    return answer