# Problem: Robot Collisions
# Platform: LeetCode
# Difficulty: Hard
# Topic: Stack, Simulation, Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(n)
class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        # Step 1: Sort robots by position
        robots = sorted(
            [(positions[i], healths[i], directions[i], i) for i in range(n)]
        )
        stack = []  # indices of robots moving right
        healths = [r[1] for r in robots]  # mutable health list
        # Step 2: Process collisions
        for i in range(n):
            pos, h, d, idx = robots[i]
            if d == 'R':
                stack.append(i)
            else:  # moving left
                while stack and healths[i] > 0:
                    j = stack[-1]

                    if healths[j] < healths[i]:
                        stack.pop()
                        healths[i] -= 1
                        healths[j] = 0
                    elif healths[j] > healths[i]:
                        healths[j] -= 1
                        healths[i] = 0
                        break
                    else:
                        stack.pop()
                        healths[i] = 0
                        healths[j] = 0
                        break
        # Step 3: Collect survivors
        res = []
        for i in range(n):
            if healths[i] > 0:
                res.append((robots[i][3], healths[i]))  # original index
        # Step 4: Restore original order
        res.sort()
        return [h for _, h in res]
