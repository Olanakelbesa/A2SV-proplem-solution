class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        nums.sort()
        count = 0
        while l < r:
            if nums[l] + nums[r] > k:
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                count += 1
                l += 1
                r -= 1
        return count