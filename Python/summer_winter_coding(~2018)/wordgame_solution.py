# programmers coding test practice:
# Summer/Winter Coding(~2018) - 영어 끝말잇기
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def wordgame_solution(n, words):
    answer = [0, 0]
    
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[0:i]:
            answer[0] = (i % n) +1
            answer[1] = (i // n) +1
            break
        

    return answer