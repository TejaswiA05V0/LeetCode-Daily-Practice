# Problem: Find All Possible Stable Binary Arrays I
# Platform: LeetCode
# Difficulty: Medium
# Topic: Dynamic Programming (Tabulation)
# Link: https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/
# Time Complexity: O(zero * one * limit)
# Space Complexity: O(zero * one)

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        # Base cases
        for i in range(1, min(limit, zero) + 1):
            dp0[i][0] = 1

        for j in range(1, min(limit, one) + 1):
            dp1[0][j] = 1

        for i in range(1, zero + 1):
            for j in range(1, one + 1):

                # Ending with 0
                for k in range(1, min(limit, i) + 1):
                    dp0[i][j] = (dp0[i][j] + dp1[i - k][j]) % MOD

                # Ending with 1
                for k in range(1, min(limit, j) + 1):
                    dp1[i][j] = (dp1[i][j] + dp0[i][j - k]) % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD
