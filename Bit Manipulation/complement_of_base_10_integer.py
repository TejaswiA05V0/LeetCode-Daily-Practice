# Problem: Complement of Base 10 Integer
# Platform: LeetCode
# Difficulty: Easy
# Topic: Bit Manipulation
# Link: https://leetcode.com/problems/complement-of-base-10-integer/
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        mask = 1

        # Create mask with all bits = 1 (same length as n)
        while mask <= n:
            mask <<= 1

        return (mask - 1) ^ n
