// programmers coding test practice:
// 연습문제 - 자릿수 더하기
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

import java.util.Arrays;

class Kim_Solution {
    public String solution(String[] seoul) {
        int x = Arrays.asList(seoul).indexOf("Kim");
        return "김서방은 " + x + "에 있다";
    }
}