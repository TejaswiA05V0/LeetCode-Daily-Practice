# Problem: Generate String Based on Constraints
# Platform: LeetCode
# Difficulty: Medium/Hard
# Topic: Strings, Greedy, Simulation
# Time Complexity: O(n * m)
# Space Complexity: O(n + m)

class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        # Result string
        s = ["a"] * (n + m - 1)
        fixed = [False] * (n + m - 1)
        # Step 1: Handle 'T' (must match)
        for i, ch in enumerate(str1):
            if ch == "T":
                for j, c in enumerate(str2, i):
                    if fixed[j] and s[j] != c:
                        return ""
                    s[j] = c
                    fixed[j] = True
        # Step 2: Handle 'F' (must differ)
        for i, ch in enumerate(str1):
            if ch == "F":
                # If already different → good
                if any(s[j] != str2[j - i] for j in range(i, i + m)):
                    continue
                # Otherwise, force a difference
                for j in range(i + m - 1, i - 1, -1):
                    if not fixed[j]:
                        s[j] = "b"   # change from 'a' to 'b'
                        break
                else:
                    return ""
        return "".join(s)
