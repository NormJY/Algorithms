# programmers coding test practice:
# 정렬 - 가장 큰 수
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def largest_solution(numbers):
    # numbers 리스트의 모든 요소를 string 타입으로 변경합니다. 이 때 map함수를 이용하여 간단히 구현할 수 있습니다.
    # 이를 리스트로 받아 numbers list를 업데이트 해줍니다. 모든 요소가 문자열 형태인 배열이 됩니다.
    numbers = list(map(str, numbers))
    
    # lambda 함수를 이용하여 재정렬해줍니다. key 인자에 lambda 함수를 추가하여 역정렬을 할 것입니다.
    # 여기서 string을 세 개까지 고려한 이유는 문제의 제한사랑에 numbers의 원소가 1000 이하인 양수와 0이기 때문입니다.
    numbers.sort(key = lambda x: x*3, reverse=True)
    
    # key의 기준으로 재정렬된 numbers의 모든 요소를 순차적으로 연결시키고(.join), 해당 문자열을 answer로 지정합니다.
    # 원래대로라면 join 메서드를 거치고 나면 string으로 자동반환되는데, 테스트 11에서 통과하지 못했습니다.
    # 하여 int로 수정했다가 string으로 다시 받은 결과를 answer에 저장하도록 했습니다. 그 결과 테스트 11까지도 무사히 작동합니다.
    answer = str(int(''.join(numbers)))
    return answer