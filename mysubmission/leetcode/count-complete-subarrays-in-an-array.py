class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        L = len(set(nums))
        l, res = 0, 0
        c, n = Counter(), len(nums)

        for r, v in enumerate(nums):
            c[v] += 1
            while len(c) == L:
                res += n-r
                c[nums[l]] -= 1
                if c[nums[l]] == 0:
                    c.pop(nums[l])
                l += 1
        return res