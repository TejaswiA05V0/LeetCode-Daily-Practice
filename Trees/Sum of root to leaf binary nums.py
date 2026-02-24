# Problem: Sum of Root To Leaf Binary Numbers
# Platform: LeetCode
# Difficulty: Easy
# Topic: Trees, DFS, Recursion
# Link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/solutions/?envType=daily-question&envId=2026-02-24
# Time Complexity: O(n)
# Space Complexity: O(h)  # h = height of tree (recursion stack)

from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current):
            if not node:
                return 0
            # Build binary number
            current = current * 2 + node.val
            # If leaf node
            if not node.left and not node.right:
                return current
            # Return sum of left and right subtree
            return dfs(node.left, current) + dfs(node.right, current)
        return dfs(root, 0)
