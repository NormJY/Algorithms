// programmers coding test practice:
// 연습문제 - 문자열 다루기 기본
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

class Strcheck_Solution {
    public static boolean solution(String s) {
        boolean answer = false;
        int s_len = s.length(); //문자열의 길이 확인
        
        if (s_len == 4 || s_len == 6){
            if (s.matches("^\\d+$")){
                return true;
            }
        }
        
        return answer;
    }
}