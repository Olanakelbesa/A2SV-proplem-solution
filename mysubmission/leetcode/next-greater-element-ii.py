class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []

        res = [-1]*len(nums)
        for i, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                r,value =  stack.pop()
                res[r]=num
            stack.append((i,num))
        if stack:
            for i, num in enumerate(nums):
                while stack and stack[-1][1] < num:
                    r,value =  stack.pop()
                    res[r]=num
    
        return res