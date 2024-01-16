class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum_ = 0
        for i in range(n):
            sum_ += nums[i]
            nums[i] = sum_
        return nums