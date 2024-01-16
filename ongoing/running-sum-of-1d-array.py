class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0]*n
        sum_ = 0
        for i in range(n):
            sum_ += nums[i]
            arr[i] = sum_
        return arr