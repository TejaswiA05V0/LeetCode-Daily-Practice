# Problem: Sort Integers by The Number of 1 Bits
# Platform: LeetCode
# Difficulty: Easy
# Topic: Bit Manipulation, Sorting
# Link:https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/?envType=daily-question&envId=2026-02-25
# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution:
    def sortByBits(self, arr):
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
