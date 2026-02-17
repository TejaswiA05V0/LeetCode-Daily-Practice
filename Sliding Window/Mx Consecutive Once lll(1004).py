# Problem: Max Consecutive Ones III
# Platform: LeetCode
# Difficulty: Medium
# Topic: Sliding Window, Arrays
# Link: https://leetcode.com/problems/max-consecutive-ones-iii/
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = 0
        maxLen = 0
        zeros = 0

        while right < n:
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)
            right += 1

        return maxLen
