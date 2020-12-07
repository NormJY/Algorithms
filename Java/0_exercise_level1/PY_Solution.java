// programmers coding test practice:
// 연습문제 - 문자열 내 p와 y의 개수
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

class PY_Solution {
    boolean solution(String s) {
        
        s = s.toUpperCase();
        int cntp = 0, cnty = 0;
        for(int i=0; i<s.length(); ++i){
            String word = s.substring(i, i+1);
            if(word.equals("P")) cntp++;
            else if(word.equals("Y")) cnty++;
        }

        return cntp == cnty;
    }
}