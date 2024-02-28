# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        res = []
        def inorder(root, flag):
            if root is None:
                return
            inorder(root.left, 'l')
            res.append((root.val, flag))
            inorder(root.right, 'r')
        inorder(root, 'l')
        
        print(res)
        l = 0
        r = len(res) - 1
        while l < r:
            if res[l][0] != res[r][0] or res[l][1] == res[r][1]:
                return False
            l += 1
            r -= 1
        return True