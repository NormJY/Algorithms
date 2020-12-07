// programmers coding test practice:
// 연습문제 - 문자열 다루기 기본
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.


class IntSum_Solution {
    public long solution(int a, int b) {
        long answer = 0;
        
        if (a < b){
            for (int i = a; i <= b; i++){
                answer += i;
            }
        } else if (a == b){
            answer = a;
        } else{
            for (int i = b; i <= a; i++){
                answer += i;
            }
        }
        return answer;
        }
    }