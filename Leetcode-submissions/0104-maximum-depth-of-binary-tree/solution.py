# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''if not root : 
            return 0
        return 1 + max(self.maxDepth(root.left) , self.maxDepth(root.right))'''
        if not root:
            return 0
            # if there is no elemnt in the tree
        level = 0  # to keep track of the level
        q =deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
