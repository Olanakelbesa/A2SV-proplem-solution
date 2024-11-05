class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        resualt = []
        _max = 0
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
              stack.append(i)

        _max = 0
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                _max = max(_max, j - stack.pop())

        return _max