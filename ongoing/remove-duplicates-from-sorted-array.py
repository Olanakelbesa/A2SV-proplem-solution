class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n =  len(nums)
        l = 0
        r = 1
        while r < n:
            if nums[l] == nums[r]:
                nums.remove(nums[r])
                n-=1
            elif nums[l] != nums[r]:
                l += 1
                r += 1
            else:
                r += 1

        print(nums)
        return len(nums)
#   0   1   2   3   3   4
#           ^   ^
