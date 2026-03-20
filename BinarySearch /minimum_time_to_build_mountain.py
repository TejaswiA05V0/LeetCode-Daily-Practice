# Problem: Minimum Number of Seconds to Make Mountain Height Zero
# Platform: LeetCode
# Difficulty: Medium
# Topic: Binary Search, Math
# Time Complexity: O(n * log(maxTime))
# Space Complexity: O(1)

from typing import List

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        maxWorkerTimes = max(workerTimes)

        l = 1
        r = maxWorkerTimes * mountainHeight * (mountainHeight + 1) // 2
        ans = 0
        eps = 1e-7

        while l <= r:
            mid = (l + r) // 2
            cnt = 0

            for t in workerTimes:
                work = mid // t

                # Solve k(k+1)/2 <= work
                k = int((-1 + (1 + 8 * work) ** 0.5) / 2 + eps)
                cnt += k

            if cnt >= mountainHeight:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
