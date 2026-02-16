# Problem: Reverse Bits
# Platform: LeetCode
# Difficulty: Easy
# Topic: Bit Manipulation
# Link: https://leetcode.com/problems/reverse-bits/
# Time Complexity: O(1)   (32 iterations, constant time)
# Space Complexity: O(1)

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        
        return result
