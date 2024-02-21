class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        steps = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                div = math.ceil(nums[i] / nums[i+1])
                nums[i] = nums[i] // div
                steps += div-1
        return steps

                 
                


