class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        lst = nums[n:]
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(lst[i])
        return result