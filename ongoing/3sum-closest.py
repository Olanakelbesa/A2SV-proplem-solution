class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float("inf")
        sum_ = float("inf")
        for i in range(len(nums)): 
            l = i+1
            r = len(nums)-1
            while l<r: 
                curSum = nums[i]+nums[l]+nums[r]
                if abs(target-curSum) < abs(target-sum_): 
                    sum_ = curSum 
                    res = sum_ 
                if curSum < target: 
                    l+= 1
                elif curSum > target: 
                    r-= 1
                else: 
                    return target 

        return res