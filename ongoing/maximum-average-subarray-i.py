class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = sum(nums[:k]) / k
        sum_num = sum(nums[:k])
        for right in range(k, len(nums)):
            sum_num = sum_num - nums[right - k] + nums[right]
            avg = max((sum_num/k), avg)
        return avg