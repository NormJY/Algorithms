// programmers coding test practice:
// 정렬 - K번째수
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

import java.util.Arrays;

class Kth_Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for (int i=0; i<commands.length; i++) {
            int[] result = new int[commands[i][1] - (commands[i][0] - 1)];
            for (int j=0; j<result.length; j++){
                result[j] = array[j + commands[i][0] - 1];
            }
            Arrays.sort(result);
            answer[i] = result[commands[i][2] - 1];
        }
        
        
        return answer;
    }
}