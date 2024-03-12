class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = (10**9 + 7)
        r = len(nums) - 1
        res = 0
        for i, left in enumerate(nums):
            while (left + nums[r]) > target and i <= r:
                r -= 1
            if i <= r:
                res += (2**(r - i))
                res %= mod
            
        return res

