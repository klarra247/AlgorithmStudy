import java.util.*;

class Solution {
    public int solution(String[] s1, String[] s2) {
        Set<String> set1 = new HashSet<>(Arrays.asList(s1));
        set1.retainAll(Arrays.asList(s2));
        
        return set1.size();
    }
}