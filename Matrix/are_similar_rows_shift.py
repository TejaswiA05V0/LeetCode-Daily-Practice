# Problem: Are Rows Similar After Shift
# Platform: Custom / LeetCode-style
# Difficulty: Medium
# Topic: Matrix, Modulo, Row Shifts
# Time Complexity: O(m*n)
# Space Complexity: O(1)
class Solution:
    def areSimilar(self, mat, k):
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if i % 2 == 0:
                    # even row: left shift by k
                    if mat[i][j] != mat[i][(j + k) % n]:
                        return False
                else:
                    # odd row: right shift by k
                    if mat[i][j] != mat[i][(j - k) % n]:
                        return False
        return True
