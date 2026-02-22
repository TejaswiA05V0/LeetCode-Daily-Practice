# Problem: Binary Gap
# Platform: LeetCode
# Difficulty: Easy
# Topic: Bit Manipulation
# Link: https://leetcode.com/problems/binary-gap/description/?envType=daily-question&envId=2026-02-22
# Time Complexity: O(log n)
# Space Complexity: O(1)
class Solution:
    def binaryGap(self, n: int) -> int:
        last = -1
        max_gap = 0
        position = 0
        while n > 0:
            if n & 1:
                if last != -1:
                    max_gap = max(max_gap, position - last)
                last = position
            n >>= 1
            position += 1
        return max_gap
