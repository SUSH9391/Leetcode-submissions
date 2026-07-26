# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # identicality of the trees can be found using if the nodes.val of the trees are same and they are having the same structure
        # both should have left and right child and should have node.val same 
        # step 1 check if structure of the tree is same 
        # step 2 check their value
        # 3 base cases 
        # a. if both trees are null return true 
        # b. if any one of them are null then return false
        # c. check the root value and if they are not alike then return false

        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False
        return (self.isSameTree(p.left , q.left) and self.isSameTree(p.right, q.right))
