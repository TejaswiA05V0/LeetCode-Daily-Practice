# Problem: Binary Watch
# Platform: LeetCode
# Difficulty: Easy
# Topic: Bit Manipulation, Brute Force
# Link: https://leetcode.com/problems/binary-watch/
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def readBinaryWatch(self, turnedOn: int):
        result = []
        
        for hour in range(12):
            for minute in range(60):
                if (hour.bit_count() + minute.bit_count()) == turnedOn:
                    result.append(f"{hour}:{minute:02d}")
        
        return result
