class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        right = []
        left = []
        middle = []
        for i in range(len(nums)):
            if nums[i] <pivot:
                left.append(nums[i])
            elif nums[i] > pivot:
                right.append(nums[i])
            else:
                middle.append(nums[i])
        result = left + middle + right
        return result