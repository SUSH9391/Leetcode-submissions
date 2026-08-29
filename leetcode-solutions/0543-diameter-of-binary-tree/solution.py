# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self,root: TreeNode) -> int:
        self.max_diameter = 0
        
        def get_height(node):
            if not node:
                return 0
                
            # Get the heights of left and right subtrees
            left_h = get_height(node.left)
            right_h = get_height(node.right)
            
            # The diameter passing through this current node is left_h + right_h
            self.max_diameter = max(self.max_diameter, left_h + right_h)
            
            # Return the actual height of this node up to its parent
            return max(left_h, right_h) + 1
            
        get_height(root)
        return self.max_diameter
