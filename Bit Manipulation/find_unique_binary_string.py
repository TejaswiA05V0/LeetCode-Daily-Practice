# Problem: Find Unique Binary String
# Platform: LeetCode
# Difficulty: Medium
# Topic: Bit Manipulation, Strings
# Link: https://leetcode.com/problems/find-unique-binary-string/
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        integers = set()

        # Convert binary strings to integers
        for num in nums:
            integers.add(int(num, 2))

        n = len(nums)

        # Find smallest missing number
        for num in range(n + 1):
            if num not in integers:
                ans = bin(num)[2:]
                return "0" * (n - len(ans)) + ans

        return ""
