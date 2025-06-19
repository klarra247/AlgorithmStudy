class Solution {
    public String solution(String my_string) {
        String answer = "";
        
        String[] arr = my_string.split("");
        
        for (String s : arr) {
            if (s.equals(s.toLowerCase())) {
                answer += s.toUpperCase();
            } else {
                answer += s.toLowerCase();
            }
        }
        return answer;
    }
}