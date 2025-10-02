class Solution {
    
    public int solution(int m, int n, int[][] puddles) {
        
        int[][] dp = new int[m + 1][n + 1];
        boolean[][] puddle = new boolean[m + 1][n + 1];
        
        for (int[] p : puddles) {
            puddle[p[0]][p[1]] = true;
        }
        
        dp[1][1] = 1; // 시작점
        
        for (int x = 1; x <= m; x++) {
            for (int y = 1; y <= n; y++) {
                if (x == 1 && y == 1) continue;
                if (puddle[x][y]) {
                    dp[x][y] = 0;
                } else {
                    dp[x][y] = (dp[x - 1][y] + dp[x][y - 1]) % 1000000007; 
                }
                
            }
        }
        
        return dp[m][n];
        
    }
}
