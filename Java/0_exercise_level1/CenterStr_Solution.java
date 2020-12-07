// programmers coding test practice:
// 연습문제 - 가운데 글자 가져오기
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

// 변수 타입을 handling 하는 게 익숙치 않아 조금 헤맸습니다.
// 원래는 charAt() 메서드를 이용하여 가운데 글자만 들고 오려고 했으나,
// char 타입과 String 타입이 다른 관계로 애를 좀 먹었습니다.

class CenterStr_Solution {
    public String solution(String s) {
        String answer = "";
        int len = s.length();
        
        if (len % 2 != 0){
            answer = s.substring(len/2, len/2+1);
        } else{
            answer = s.substring(len/2-1, len/2+1);
        }
        return answer;
    }
}