// programmers coding test practice:
// 연습문제 - 약수의 합
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.


class DivisorSum_Solution {
    public int solution(int n) {
        int answer = 0;
        
        for (int i = 1; i < n+1; i++){
            if (n % i == 0){
                answer += i;
            }
        }
        return answer;
    }
}