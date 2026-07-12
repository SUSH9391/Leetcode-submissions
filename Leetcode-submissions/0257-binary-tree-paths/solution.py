# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root):
            if root is None:
                return []
            if root.left is None and root.right is None:
                return [str(root.val)] #when there is only 1 element in the tree
            paths = []
            for path in dfs(root.left):
                paths.append(f"{root.val}->{path}")

            for path in dfs(root.right):
                paths.append(f"{root.val}->{path}")
            return paths
        return dfs(root)
