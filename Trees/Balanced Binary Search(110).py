# Problem: Balanced Binary Tree
# Platform: LeetCode
# Difficulty: Easy
# Topic: Trees, Depth First Search (DFS), Recursion
# Link: https://leetcode.com/problems/balanced-binary-tree/
# Time Complexity: O(n)
# Space Complexity: O(h)  # h = height of tree (recursion stack)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root):
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            if left == -1:
                return -1

            right = height(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return height(root) != -1
