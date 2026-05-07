import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums[:]

        # Key insight 1: every edge i→j has a reverse j→i (the graph is undirected).
        #   Forward edge (j>i, nums[j]<nums[i]) always pairs with
        #   backward edge (i<j, nums[i]>nums[j]) — same condition, both directions.
        #
        # Key insight 2: connected components are always contiguous intervals.
        #   If nodes i and k are connected (i<k), every j between them is too,
        #   because it either forms a direct inversion with i or k, or chains through them.
        #
        # Key insight 3: a component boundary exists between i and i+1 iff
        #   max(nums[0..i]) <= min(nums[i+1..n-1])
        #   — meaning no value on the left exceeds any on the right,
        #   so no inversion can cross that boundary.
        #
        # Key insight 4: the answer for every node in a component is the component maximum,
        #   since all nodes are mutually reachable (undirected connected component).

        # Build prefix max left→right
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])

        # Build suffix min right→left
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        # Single sweep: assign component max to each element
        ans = [0] * n
        start = 0
        for i in range(n - 1):
            if prefix_max[i] <= suffix_min[i + 1]:   # clean boundary here
                for k in range(start, i + 1):
                    ans[k] = prefix_max[i]            # = max of this component
                start = i + 1
        for k in range(start, n):                     # last component
            ans[k] = prefix_max[n - 1]

        return ans