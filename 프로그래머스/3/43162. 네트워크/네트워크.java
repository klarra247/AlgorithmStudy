import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                stack.push(i);
                answer += 1;
                 while (!stack.isEmpty()) {
                     int v = stack.pop();

                     if (!visited[v]) {
                         visited[v] = true;

                         for (int j = 0; j < n; j++) {
                             if (computers[v][j] == 1 && !visited[j]) {
                                 stack.push(j);
                             }
                         }
                     }
                 }
            }
        }
        
        return answer;
    }
}