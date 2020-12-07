// programmers coding test practice:
// 연습문제 - 행렬의 덧셈
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.


import java.lang.Math;

class MatSum_Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int row = Math.max(arr1.length, arr2.length);
        int col = Math.max(arr1[0].length, arr2[0].length);
        int[][] answer = new int[row][col];
        
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                answer[i][j] = arr1[i][j] + arr2[i][j];
            }
        }
        
        return answer;
    }
}