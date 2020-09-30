# programmers coding test practice:
# 연습문제 - 서울에서 김서방 찾기
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def kim_solution(seoul):
    
    x = seoul.index("Kim")
    answer = "김서방은 " + str(x) + "에 있다"
    
    return answer