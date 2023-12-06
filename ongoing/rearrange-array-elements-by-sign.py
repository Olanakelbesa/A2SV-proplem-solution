class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive = []
        negative = []
        result = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        for i in range(len(nums)/2):
            result.append(positive[i])
            result.append(negative[i])
        print(result)
        return result