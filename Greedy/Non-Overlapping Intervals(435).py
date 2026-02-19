# Problem: Non-overlapping Intervals
# Platform: LeetCode
# Difficulty: Medium
# Topic: Greedy, Intervals, Sorting
# Link: https://leetcode.com/problems/non-overlapping-intervals/description/
# Time Complexity: O(n log n)
# Space Complexity: O(1)

from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        count = 1
        endTime = intervals[0][1]
        for row in range(1, n):
            if intervals[row][0] >= endTime:
                count += 1
                endTime = intervals[row][1]
        return n - count
