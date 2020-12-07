// programmers coding test practice:
// 연습문제 - 제일 작은 수 제거하기
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.


import java.util.*;
class RemoveMin_Solution {
  public int[] solution(int[] arr) {
      int[] answer = {};
	      int min = arr[0];
	      if(arr.length==1){
	          return new int[]{-1};
	      }
	      for(int i =0; i<arr.length; i++){
	          min = Math.min(arr[i],min);
	      }
	      answer = new int[arr.length-1];
	      
	      int j =0;
	      for(int i =0; i<answer.length; i++){
	          if(arr[j] == min){
	              j++;
	              i--;
	              continue;
	          }
	          answer[i] = arr[j];
	          j++;
	      }
	      return answer;
  }
}