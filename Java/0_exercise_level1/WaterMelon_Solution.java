// programmers coding test practice:
// 연습문제 - 수박수박수박수박수박수?
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

class WaterMelon_Solution {
    public String solution(int n) {

        return new String(new char [n/2+1]).replace("\0", "수박").substring(0,n);
    }
}