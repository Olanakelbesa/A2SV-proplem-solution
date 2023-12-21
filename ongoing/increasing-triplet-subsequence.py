class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        i = max(nums)
        j = max(nums)
        for k in range(n):
            if nums[k] <= i:
                i = nums[k]
            elif nums[k] <= j:
                j = nums[k]
            else:
                return True
        return False
            