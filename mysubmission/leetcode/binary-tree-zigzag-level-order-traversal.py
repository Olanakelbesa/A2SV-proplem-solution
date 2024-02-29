# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        def helper(root, level):
            if root is None:
                return 
            if level % 2 == 0:
                dic[level].append(root.val)
            else:
                dic[level].insert(0, root.val)

            helper(root.left, level+1)
            helper(root.right, level+1)
        helper(root, 0)
        return list(dic.values())
            