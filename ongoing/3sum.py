class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        for i in range(len(nums)-2):
            if  (nums[i]>0 ):return res
            l,r=i+1,len(nums)-1
            t=nums[i]+nums[l]+nums[r]
            while(  r>l):
                if t>0:
                    r-=1
                elif t<0:
                    l+=1
                else:
                    res.add((nums[i],nums[l],nums[r]))
                    r-=1
                    l+=1
                t=nums[i]+nums[l]+nums[r]
        return res