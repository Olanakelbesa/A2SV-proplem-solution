class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        curSum = 0
        dic = {}
        count = 0
        for i in range(len(nums)):
            if curSum in dic:
                dic[curSum] +=1
            else:
                dic[curSum] = 1
            curSum += nums[i]    

            if (curSum - goal) in dic: 
                count += dic[curSum - goal] 
        return count