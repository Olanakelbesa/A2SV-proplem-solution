class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)//2):
            freq = nums[2*i]
            val = nums[2*i+1]
            for i in range(freq):
                result.append(val)
        return result