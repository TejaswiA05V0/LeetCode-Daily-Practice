# Problem: Check if Strings Can Be Made Equal With Operations I
# Platform: LeetCode
# Difficulty: Easy
# Topic: Strings, Swapping
# Time Complexity: O(1)
# Space Complexity: O(1)
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return (
            ((s1[0] == s2[0] and s1[2] == s2[2]) or
             (s1[0] == s2[2] and s1[2] == s2[0])) and
            ((s1[1] == s2[1] and s1[3] == s2[3]) or
             (s1[1] == s2[3] and s1[3] == s2[1]))
        )
