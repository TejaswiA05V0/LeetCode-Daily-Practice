# Problem: Two Sum
# Platform: LeetCode
# Difficulty: Easy
# Topic: Arrays, HashMap
# Link: https://leetcode.com/problems/two-sum/
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i
