# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def helper(root, max_val, min_val):
            if root is None:
                return (max_val - min_val)
            max_val = max(root.val, max_val)
            min_val = min(root.val, min_val)
            return max(helper(root.left, max_val, min_val), helper(root.right, max_val, min_val))

        return helper(root, -inf, inf)