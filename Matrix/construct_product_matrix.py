# Problem: Construct Product Matrix
# Platform: LeetCode
# Difficulty: Medium
# Topic: Matrix, Prefix Product, Math
# Link: https://leetcode.com/problems/construct-product-matrix/
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def constructProductMatrix(self, grid):
        MOD = 12345
        m, n = len(grid), len(grid[0])
        # Flatten grid
        arr = []
        for i in range(m):
            for j in range(n):
                arr.append(grid[i][j] % MOD)
        size = len(arr)
        # Prefix and suffix products
        prefix = [1] * size
        suffix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i - 1] * arr[i - 1]) % MOD
        for i in range(size - 2, -1, -1):
            suffix[i] = (suffix[i + 1] * arr[i + 1]) % MOD
        # Build result matrix
        res = [[0] * n for _ in range(m)]
        for idx in range(size):
            val = (prefix[idx] * suffix[idx]) % MOD
            i, j = divmod(idx, n)
            res[i][j] = val
        return res
