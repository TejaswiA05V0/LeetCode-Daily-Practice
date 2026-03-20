# Problem: Largest Submatrix With Rearrangements
# Platform: LeetCode
# Difficulty: Medium
# Topic: Matrix, Greedy, Sorting
# Link: https://leetcode.com/problems/largest-submatrix-with-rearrangements/
# Time Complexity: O(m * n log n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        prev_row = [0] * n
        ans = 0

        for row in range(m):
            curr_row = matrix[row][:]

            # Build heights
            for col in range(n):
                if curr_row[col] != 0:
                    curr_row[col] += prev_row[col]

            # Sort heights in descending order
            sorted_row = sorted(curr_row, reverse=True)

            # Calculate max area
            for i in range(n):
                ans = max(ans, sorted_row[i] * (i + 1))

            prev_row = curr_row

        return ans
