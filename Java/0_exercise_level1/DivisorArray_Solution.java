// programmers coding test practice:
// 연습문제 - 나누어 떨어지는 숫자 배열
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

import java.util.Arrays;

class DivisorArray_Solution {
  public int[] solution(int[] arr, int divisor) {
          int[] answer = Arrays.stream(arr).filter(factor -> factor % divisor == 0).toArray();
          if(answer.length == 0) answer = new int[] {-1};
          java.util.Arrays.sort(answer);
          return answer;
  }
}