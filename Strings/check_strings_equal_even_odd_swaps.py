# Problem: Check if Strings Can Be Made Equal With Operations II
# Platform: LeetCode
# Difficulty: Medium
# Topic: Strings, Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even1 = sorted(s1[i] for i in range(0, len(s1), 2))
        even2 = sorted(s2[i] for i in range(0, len(s2), 2))
        
        odd1 = sorted(s1[i] for i in range(1, len(s1), 2))
        odd2 = sorted(s2[i] for i in range(1, len(s2), 2))
        
        return even1 == even2 and odd1 == odd2
