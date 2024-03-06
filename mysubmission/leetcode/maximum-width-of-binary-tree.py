# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = []
        def perorder(root, level, idx):
            if not root:
                return
            left = perorder(root.left, level + 1,  2*idx )
            right = perorder(root.right, level + 1, 2*idx + 1)
            res.append((level, idx))
        perorder(root, 1, 1)

        dic = defaultdict(list)
        for i in range(len(res)):
            dic[res[i][0]].append(res[i][1])

        max_width = 1

        for key, val in dic.items():
            if len(dic[key]) > 1:
                num = dic[key]
                diff = (num[-1] - num[0])
                max_width = max(max_width, (diff+1))

        return max_width
