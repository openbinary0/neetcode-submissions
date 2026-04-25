# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # pre-order DFS, i.e. swap children before swapping the parents
        if root is None:
            return
        # swap children:
        self.invertTree(root.left)
        self.invertTree(root.right)
        # swap parent:
        temp = root.left
        root.left = root.right
        root.right = temp
        # return
        return root