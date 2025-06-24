class Solution {
    public int solution(int n) {
        int answer = n;
        String binary = Integer.toBinaryString(n);
        int num = String.valueOf(binary).replace("0", "").length();
        Boolean bool = true;
        while (bool) {
            answer = answer += 1;
            binary = Integer.toBinaryString(answer);
            if (num == String.valueOf(binary).replace("0", "").length()) return answer;
        }
        
        return answer;
        
    }
}