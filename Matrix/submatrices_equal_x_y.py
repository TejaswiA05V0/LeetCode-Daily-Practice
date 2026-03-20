# Problem: Count Submatrices with Equal X and Y (including (0,0))
# Platform: LeetCode
# Difficulty: Medium
# Topic: Matrix, Prefix Sum
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])
        # Prefix sums for X and Y
        px = [[0] * (n + 1) for _ in range(m + 1)]
        py = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                px[i + 1][j + 1] = px[i][j + 1] + px[i + 1][j] - px[i][j]
                py[i + 1][j + 1] = py[i][j + 1] + py[i + 1][j] - py[i][j]
                if grid[i][j] == 'X':
                    px[i + 1][j + 1] += 1
                elif grid[i][j] == 'Y':
                    py[i + 1][j + 1] += 1
        def get_sum(pref, r1, c1, r2, c2):
            return pref[r2 + 1][c2 + 1] - pref[r1][c2 + 1] - pref[r2 + 1][c1] + pref[r1][c1]
        count = 0
        # Only submatrices starting at (0,0)
        for r2 in range(m):
            for c2 in range(n):
                x_count = get_sum(px, 0, 0, r2, c2)
                y_count = get_sum(py, 0, 0, r2, c2)

                if x_count > 0 and x_count == y_count:
                    count += 1
        return count
