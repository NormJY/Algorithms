# programmers coding test practice:
# 연습문제 - 문자열 내 마음대로 정렬하기
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def customsort_solution(strings, n):
    # 테스트 케이스 2번과 같은 경우에도 잘 작동하는 함수를 위해,
    # 다음과 같이 strings를 한 번 정렬한 후에 n번째 인덱스를 기준으로 재정렬했습니다.
    answer = sorted(sorted(strings), key=lambda strings: strings[n])
    
    return answer