# Problem: Determine Whether Matrix Can Be Obtained By Rotation
# Platform: LeetCode
# Difficulty: Easy
# Topic: Matrix, Simulation
# Link: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/
# Time Complexity: O(n^2)
# Space Complexity: O(1)

from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        # Try all 4 rotations
        for _ in range(4):

            # Rotate matrix 90 degrees clockwise (in-place)
            for i in range(n // 2):
                for j in range((n + 1) // 2):
                    (
                        mat[i][j],
                        mat[n - 1 - j][i],
                        mat[n - 1 - i][n - 1 - j],
                        mat[j][n - 1 - i],
                    ) = (
                        mat[n - 1 - j][i],
                        mat[n - 1 - i][n - 1 - j],
                        mat[j][n - 1 - i],
                        mat[i][j],
                    )

            if mat == target:
                return True

        return False
