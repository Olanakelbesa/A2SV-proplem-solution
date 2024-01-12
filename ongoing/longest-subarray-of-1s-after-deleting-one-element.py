class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        s = 0
        k = 1

        if 0 not in nums:
            return len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == 0:
                k -= 1
            if k < 0:
                if nums[s] == 0:
                    k += 1
                s += 1
        return i - s

            

            