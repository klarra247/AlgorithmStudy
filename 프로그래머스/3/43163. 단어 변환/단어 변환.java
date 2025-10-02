import java.util.*;
class Solution {
    
    public boolean differOne(String word1, String word2) {
        int diff = 0;
        for (int i = 0; i < word1.length(); i++){
            if (word1.charAt(i) != word2.charAt(i)) {
                diff += 1;
                if (diff > 1) return false;
            }
        }
        return diff == 1;
    }
    
    public int solution(String begin, String target, String[] words) {
        // target이 words에 없으면 0 반환
        if (!Arrays.asList(words).contains(target)) return 0;
        
        int num = words.length;
        boolean[] visited = new boolean[num];
        
        // BFS: 큐에 (단어 index, 현재 단계)
        Queue<int[]> queue = new LinkedList<>();
        
        // begin과 1 letter 차이 나는 단어들 큐에 넣음
        for (int i = 0; i < num; i++) {
            if (differOne(begin, words[i])) {
                queue.offer(new int[]{i, 1});
                visited[i] = true;
            }
        }
        
        while (!queue.isEmpty()) {
            int[] v = queue.poll();
            int idx = v[0];
            int depth = v[1];
            
            if (words[idx].equals(target)) return depth;
            
            for (int j = 0; j < num; j++) {
                if (differOne(words[idx], words[j]) && !visited[j]) {
                    queue.offer(new int[]{j, depth + 1});
                    visited[j] = true;
                }
            }
        }

        return 0;
    }
}