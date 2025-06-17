class Solution {
    public String solution(String my_string) {
        char[] arr = my_string.toCharArray();
        String answer = "";
        for (char letter : arr) {
            answer = letter + answer;
        }
        return answer;
    }
}