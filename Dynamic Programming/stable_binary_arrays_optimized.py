# Problem: Find All Possible Stable Binary Arrays I
# Platform: LeetCode
# Difficulty: Medium
# Topic: Dynamic Programming, Memoization
# Link: https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/
# Time Complexity: O(zero * one)
# Space Complexity: O(zero * one)

from functools import cache

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7

        @cache
        def dp(zero, one, lastBit):
            # Base cases
            if zero == 0:
                return 1 if lastBit == 1 and one <= limit else 0

            if one == 0:
                return 1 if lastBit == 0 and zero <= limit else 0

            if lastBit == 0:
                res = dp(zero - 1, one, 0) + dp(zero - 1, one, 1)

                if zero > limit:
                    res -= dp(zero - limit - 1, one, 1)
            else:
                res = dp(zero, one - 1, 0) + dp(zero, one - 1, 1)

                if one > limit:
                    res -= dp(zero, one - limit - 1, 0)

            return res % mod

        res = (dp(zero, one, 0) + dp(zero, one, 1)) % mod
        dp.cache_clear()
        return res
