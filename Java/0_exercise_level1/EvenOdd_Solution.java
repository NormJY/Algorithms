// programmers coding test practice:
// 연습문제 - 짝수와 홀수
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.


// 아주 간단한 문제입니다.
// 입력 num이 2로 나누어떨어지면 "Even", 그렇지 않은 모든 경우는 "Odd"를 출력하도록 했습니다.

class EvenOdd_Solution {
    public String solution(int num) {
        String answer = "";
        
        if (num % 2 == 0){
            answer = "Even";
        } else{
            answer = "Odd";
        }
        return answer;
    }
}