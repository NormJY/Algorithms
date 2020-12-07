// programmers coding test practice:
// 연습문제 - 하샤드 수
// 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

class Harshad_Solution {
    public boolean solution(int x) {
        boolean answer = true;  // 기본값으로 true를 설정해 줍니다.
        String sx = Integer.toString(x);  // 수를 하나씩 들고 오기 위해 String 객체로 변경했습니다.
        int h = Integer.parseInt(sx.substring(0,1));
        
		// System.out.println(h);
        
		for (int i = 1; i<sx.length(); i++){
            h = h + Integer.parseInt(sx.substring(i,i+1));
        }
        
        // System.out.println(h);
        
		if (x % h != 0){
            answer = false;
        }
        
        return answer;
    }
}