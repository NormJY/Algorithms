// programmers coding test practice:
// 연습문제 - 자연수 뒤집어 배열로 만들기
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.



class ReverseInt_Solution {
  public int[] solution(long n) {
      String s = String.valueOf(n);
      StringBuilder sb = new StringBuilder(s);
      sb = sb.reverse();
      String[] ss = sb.toString().split("");

      int[] answer = new int[ss.length];
      for (int i=0; i<ss.length; i++) {
          answer[i] = Integer.parseInt(ss[i]);
      }
      return answer;
  }
}