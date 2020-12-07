// programmers coding test practice:
// 연습문제 - 2016년
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

// 파이썬으로 같은 문제를 풀었을 때처럼, 자바에서도 날짜 정보를 표현해주는 라이브러리가 있을 것 같아서
// 해당 라이브러리의 사용법을 참고했습니다.
// 다른 분들이 푸신 방법을 보니 하나하나 대입하는 방식으로도 풀어놓으셨네요.
// 시간이 얼마나 걸리는지는 모르겠으나, 일단 아래와 같은 코드는 테스트 1회당 1.43ms 정도로,
// 생각보다 많은 시간이 소요되었습니다. 


import java.time.*;

class DayOfWeek_Solution {
    public String solution(int a, int b) {
        LocalDate date = LocalDate.of(2016, a, b);
        return date.getDayOfWeek().toString().substring(0, 3);
    }
}