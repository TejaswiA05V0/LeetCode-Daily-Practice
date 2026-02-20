# Problem: Special Binary String
# Platform: LeetCode
# Difficulty: Hard
# Topic: Recursion, Divide & Conquer, Greedy, Strings
# Link: https://leetcode.com/problems/special-binary-string/submissions/1925376778/?envType=daily-question&envId=2026-02-20
# Time Complexity: O(n^2 log n)
# Space Complexity: O(n)

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        start = 0
        subs = []
        for i, ch in enumerate(s):
            if ch == '1':
                count += 1
            else:
                count -= 1
            # Found a primitive special substring
            if count == 0:
                # Recursively process inside
                inner = self.makeLargestSpecial(s[start + 1:i])
                subs.append("1" + inner + "0")
                start = i + 1
        # Sort descending to get lexicographically largest
        subs.sort(reverse=True)
        return "".join(subs)
