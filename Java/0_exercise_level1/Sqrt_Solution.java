// programmers coding test practice:
// 연습문제 - 정수 제곱근 판별
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

import java.lang.Math;

class Sqrt_Solution {
    public long solution(long n) {
        Double sqrt = Math.sqrt(n);
        
        if(sqrt == sqrt.intValue()){
            return (long)Math.pow(sqrt+1, 2);
        }else return -1;
        
    }
}