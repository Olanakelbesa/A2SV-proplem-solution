class Solution(object):
    def countPairs(self, nums, target):
        n = len(nums)

        nums.sort()

        c = 0
        l = 0
        r = n-1

        while l < r:
            if nums[l] + nums[r] < target:
                c += r - l
                l += 1
            else:
                r -= 1

        return c