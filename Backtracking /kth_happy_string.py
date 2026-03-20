# Problem: The k-th Lexicographical String of All Happy Strings of Length n
# Platform: LeetCode
# Difficulty: Medium
# Topic: Backtracking, Recursion, Strings
# Link: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings = []

        self.generate_happy_strings(n, "", happy_strings)

        if len(happy_strings) < k:
            return ""

        return happy_strings[k - 1]

    def generate_happy_strings(self, n: int, current_string: str, happy_strings: list):
        # If length reached, store result
        if len(current_string) == n:
            happy_strings.append(current_string)
            return

        for ch in ['a', 'b', 'c']:
            # Avoid same adjacent characters
            if current_string and current_string[-1] == ch:
                continue

            self.generate_happy_strings(n, current_string + ch, happy_strings)
