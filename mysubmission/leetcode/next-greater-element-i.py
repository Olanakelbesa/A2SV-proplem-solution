class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}

        res = [0]*len(nums1)
        for num in nums1:
            dic[num] = -1
        for num in nums2:
            while stack and stack[-1] < num:
                dic[stack.pop()] = num
            stack.append(num)
        for i in range(len(nums1)):
            res[i] = dic[nums1[i]]
        return res
