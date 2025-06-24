import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> list = new ArrayList<>();
        
        int current = -1;
        for (int i : arr) {
            if (i != current) {
                list.add(i);
                current = i;
            }
        }
        
        return list.stream().mapToInt(i -> i).toArray();
    }
}