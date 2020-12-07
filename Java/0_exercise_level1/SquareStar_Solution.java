// programmers coding test practice:
// 연습문제 - 직사각형 별찍기
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

// Scanner 모듈을 통해 입력을 전달받습니다.

import java.util.Scanner;

public class SquareStar_Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        for(int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}