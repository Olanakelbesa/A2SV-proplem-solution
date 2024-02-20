class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        r, max_, res = 0, 0, 0

        while max_ < n:
            if r < len(nums) and nums[r] <= max_ + 1:
                max_ += nums[r]
                r += 1
            else:
                add = max_ + 1
                max_ += add
                res += 1
        return res
