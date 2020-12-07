// programmers coding test practice:
// 연습문제 - 문자열 내림차순으로 배치하기
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

// 알고리즘이든, 언어를 활용하여 간단한 프로그램을 작성하든,
// 대부분의 공부를 파이썬을 중심으로 하고 있었던 데다
// 자바와 같은 객체 지향 프로그래밍의 작동원리를 이해하지 못한 것인지
// 자바가 많이 어렵게만 느껴져 다른 분들의 풀이를 많이 참고하고 있습니다.

public class ReverseStr_Solution {
    public String solution(String s) {
        String[] array = s.split("");
        Arrays.sort(array);
        Collections.reverse(Arrays.asList(array));
        
        return String.join("", array);
    }

}