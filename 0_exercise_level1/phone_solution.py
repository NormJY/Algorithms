# programmers coding test practice:
# 연습문제 - 핸드폰 번호 가리기
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.


def phone_solution(phone_number):
    answer = "*"*(len(phone_number)-4) + phone_number[-4:]
    return answer