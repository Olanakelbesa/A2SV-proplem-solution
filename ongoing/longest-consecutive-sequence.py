class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 0

        nums.sort()

        count = 1
        maxi = 0

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    count += 1
                else:
                    maxi = max(maxi, count)
                    count = 1

        return max(maxi, count)