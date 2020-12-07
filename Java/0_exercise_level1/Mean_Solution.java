// programmers coding test practice:
// 연습문제 - 평균 구하기
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

class Mean_Solution {
    public double solution(int[] arr) {
        double mean = 0;
        double sum = 0;  // sum을 int로 지정하면 소수점 아래 수를 버리게 되어, 테스트 케이스 1번을 통과하지 못합니다.
        
        for (int i = 0;i<arr.length;i++){
            sum = sum + arr[i];
        }
        
        mean = sum / arr.length;
        return mean;
    }
}