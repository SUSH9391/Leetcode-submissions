# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        tilt = 0
        def dfs(node):
            nonlocal tilt
            if node is None:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            tilt += abs(left_sum - right_sum)
            return left_sum + right_sum +node.val
        dfs(root)
        return tilt
