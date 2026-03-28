# Problem: Find the String with LCP
# Platform: LeetCode
# Difficulty: Hard
# Topic: Strings, Greedy, Matrix Validation
# Time Complexity: O(n^2)
# Space Complexity: O(n)

from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = [""] * n
        current = ord("a")

        # Step 1: Construct string greedily
        for i in range(n):
            if not word[i]:
                if current > ord("z"):
                    return ""
                word[i] = chr(current)
                
                for j in range(i + 1, n):
                    if lcp[i][j]:
                        word[j] = word[i]
                
                current += 1

        # Step 2: Validate using LCP definition
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] != word[j]:
                    if lcp[i][j] != 0:
                        return ""
                else:
                    if i == n - 1 or j == n - 1:
                        if lcp[i][j] != 1:
                            return ""
                    else:
                        if lcp[i][j] != lcp[i + 1][j + 1] + 1:
                            return ""

        return "".join(word)
