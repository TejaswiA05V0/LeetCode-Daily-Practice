# Problem: Minimum Absolute Difference in k x k Submatrix
# Platform: LeetCode
# Difficulty: Medium
# Topic: Matrix, Sorting, Sliding Window
# Link: https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/description/
# Time Complexity: O((m * n) * k^2 * log(k^2))
# Space Complexity: O(k^2)

class Solution:
    def minAbsDiff(self, grid, k):
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                vals = []
                # collect elements in k x k submatrix
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.append(grid[x][y])
                vals.sort()
                # compute minimum absolute difference
                min_diff = float('inf')
                for t in range(1, len(vals)):
                    if vals[t] != vals[t - 1]:
                        min_diff = min(min_diff, vals[t] - vals[t - 1])
                ans[i][j] = 0 if min_diff == float('inf') else min_diff
        return ans
