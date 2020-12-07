// programmers coding test practice:
// 연습문제 - 정수 내림차순으로 배치하기
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

import java.util.Arrays;

class Int_Solution {
    public long solution(long n) {
        long answer = 0;
        String nstr = String.valueOf(n);
        char[] sol = nstr.toCharArray();
        Arrays.sort(sol);
        nstr = new StringBuilder(new String(sol)).reverse().toString();
        answer = Long.parseLong(nstr);
        
        return answer;
    }
}