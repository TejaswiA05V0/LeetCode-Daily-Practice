# Problem: Check If Binary String Has at Most One Segment of Ones
# Platform: LeetCode
# Difficulty: Easy
# Topic: Strings
# Link: https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s
