# programmers coding test practice:
# 스택/큐 - 프린터
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def Printer_solution(priorities, location):
    
    answer = 0
    
    while priorities != []:
        primax = max(priorities)
        doc_J = priorities.pop(0)
        if primax == doc_J:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
        else:
            priorities.append(doc_J)
            if location == 0:
                location = len(priorities) - 1  # 0번째 문서 J가 대기목록의 맨 뒤로 갔으므로, location도 업데이트
            else:
                location -= 1  # 내 요청 문서가 한 칸 앞으로 이동.
                
    return answer