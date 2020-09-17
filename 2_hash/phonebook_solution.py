# programmers coding test practice:
# 해시 - 전화번호 목록
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def phonebook_solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            answer = False
            break
    
    return answer