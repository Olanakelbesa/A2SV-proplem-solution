# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def preorder(root, add):
            if not root:
                return 0
            add = add * 10 + root.val
            if not root.left and not root.right:
                return add 
            return (preorder(root.left, add) + preorder(root.right, add))
        
        return preorder(root, 0)
