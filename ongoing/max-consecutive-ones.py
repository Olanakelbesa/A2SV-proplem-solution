class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp, window = 0, 0
        for num in nums:
            if num == 1:
                window += 1
            else:
                temp = max(temp, window)
                window = 0
        temp = max(temp, window)
        return temp

        