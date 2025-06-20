class Solution {
    public String solution(String myString) {
        String answer = "";
        String[] arr = myString.split("");
        
        for (String s : arr) {
            if (s.compareTo("l") < 0) {
                answer += "l";
            } else {
                answer += s;
            }
        }
        return answer;
    }
}