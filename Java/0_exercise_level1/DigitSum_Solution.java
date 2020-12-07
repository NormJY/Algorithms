// programmers coding test practice:
// 연습문제 - 자릿수 더하기
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

// 하샤드 수 문제를 풀었던 것에서 착안하여 풀면 쉽습니다.

public class DigitSum_Solution {
    public int solution(int n) {
        String sn = Integer.toString(n);
        int answer = Integer.parseInt(sn.substring(0,1));
        
        for (int i = 1; i<sn.length(); i++){
            answer = answer + Integer.parseInt(sn.substring(i,i+1));
        }
        
        return answer;
    }
}