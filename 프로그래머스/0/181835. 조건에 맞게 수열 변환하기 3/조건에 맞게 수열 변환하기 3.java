import java.util.*;

class Solution {
    public int[] solution(int[] arr, int k) {
        List<Integer> answer = new ArrayList<>();
        
        if (k % 2 == 1) {
            for (int a : arr) {
                answer.add(a * k);
            }
        } else {
            for (int a : arr) {
                answer.add(a + k);
            }
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}