class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        maj = n // 3
        result = []
        for i, num in enumerate(nums):
            if nums.count(num) > maj and num not in result:
                result.append(num)
        return result