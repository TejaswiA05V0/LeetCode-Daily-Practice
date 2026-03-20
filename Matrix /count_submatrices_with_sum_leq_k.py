# Problem: Count Submatrices With Sum ≤ k (from top-left)
# Platform: LeetCode
# Difficulty: Medium
# Topic: Matrix, Prefix Sum
# Time Complexity: O(n * m)
# Space Complexity: O(m)

from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        cols = [0] * m
        res = 0

        for i in range(n):
            row_sum = 0
            for j in range(m):
                cols[j] += grid[i][j]
                row_sum += cols[j]

                if row_sum <= k:
                    res += 1

        return res
