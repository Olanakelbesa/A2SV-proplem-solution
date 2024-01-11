class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=[str(i) for i in nums]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if str(nums[i])+str(nums[j])>str(nums[j])+str(nums[i]):
                    continue
                else:
                    nums[i],nums[j]=nums[j],nums[i]
        if int("".join(str(i) for i in nums))==0:
            return "0"             
        return  "".join(str(i) for i in nums)                

        