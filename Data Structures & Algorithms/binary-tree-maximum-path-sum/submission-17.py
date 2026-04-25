# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# path sum needs 2 or more nodes
# count the current sum
# find the linked list with the max sum (at least 2 nodes)

import math

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def max_path_sum(node):
            if node is None:
                return -math.inf
            sum_linear_left = max_path_sum_linear(node.left)
            sum_linear_right = max_path_sum_linear(node.right)
            return max(
                # current node is included:
                node.val,
                node.val + sum_linear_left,
                node.val + sum_linear_right,
                node.val + sum_linear_left
                         + sum_linear_right,
                # current node is not included:
                max_path_sum(node.left), max_path_sum(node.right),
            )

        def max_path_sum_linear(node):
            # current node is included
            # find a linear path (cannot select both paths)
            # can include only one node
            if node is None:
                return -math.inf
            return max(
                node.val,
                node.val + max_path_sum_linear(node.left),
                node.val + max_path_sum_linear(node.right),
            )

        return max_path_sum(root)