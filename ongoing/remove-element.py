class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        l = 0
        r = n - 1
        count = 0
        while l < r:
            if nums[l] == val and nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            else:
                if nums[l] != val:
                    l += 1
                if nums[r] == val:
                    r -= 1
        for num in nums:
            if num != val:
                count+=1
        return count



