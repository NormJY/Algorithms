# programmers coding test practice:
# 연습문제 - 이상한 문자 만들기
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

# 스트링 사용이 익숙치 않은 것 같습니다. 아무래도 다른 문제에 비해 애를 좀 먹었습니다.
# 조금 더 간단하게 풀 수 있는 방법이 있는지 찾아볼 필요가 있을 것 같습니다.
# 물론 저는 한줄 풀이를 선호하지 않기 때문에... 제 풀이보다 조금 더 간단하기만 하면 됩니다.

def weirdstr_solution(s):
    slist = []
    word = s.split(' ')
    
    for W in word:
        st = ''
        for idx, le in enumerate(W):
            if idx % 2 == 0:
                st += le.upper()
            else:
                st += le.lower()
        slist.append(st)
            
    answer = ' '.join(slist)
    
    return answer