import java.util.*;
class Solution {
    public int solution(int[] d, int budget) {
        int sum = 0;
        Arrays.sort(d);
        int i = 0;
        
        while (i < d.length && sum + d[i] <= budget) {
            sum += d[i];
            i++;            
        }

        return i;
    }
}