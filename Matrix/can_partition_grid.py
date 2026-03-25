# Problem: Partition Grid Into Two Equal Sum Parts
# Platform: LeetCode
# Difficulty: Medium
# Topic: Matrix, Prefix Sum
# Time Complexity: O(m*n)
# Space Complexity: O(n)

class Solution:
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])
        total = sum(map(sum, grid))
        # Odd total → impossible
        if total % 2 != 0:
            return False
        target = total // 2
        # Horizontal cut
        row_sum = 0
        for i in range(m - 1):
            row_sum += sum(grid[i])
            if row_sum == target:
                return True
        # Vertical cut
        col_sum = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        curr = 0
        for j in range(n - 1):
            curr += col_sum[j]
            if curr == target:
                return True
        return False
