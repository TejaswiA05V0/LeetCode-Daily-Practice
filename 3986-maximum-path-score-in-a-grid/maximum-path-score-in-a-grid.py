class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [{} for i in range(n)]
        dp[0][0] = 0 # base case: with cost 0, max score 0 
        
        for i in range(m): 
            ndp = [{} for i in range(n)]
            for j in range(n): 
                for pc in dp[j]: 
                    c = pc + min(1, grid[i][j])
                    if c <= k: 
                        ndp[j][c] = max(
                            ndp[j].get(c, -1), 
                            dp[j][pc] + grid[i][j]
                        )
                if j < n - 1: 
                    for pc in ndp[j]: 
                        c = pc + min(1, grid[i][j + 1])
                        if c <= k: 
                            ndp[j + 1][c] = max(
                                ndp[j + 1].get(c, -1), 
                                ndp[j][pc] + grid[i][j + 1]                                
                            )
            dp = ndp

        if len(dp[-1]) == 0: return -1 

        return max(dp[-1].values())
      