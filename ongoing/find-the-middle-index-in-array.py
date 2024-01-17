class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = []
        suffix = []
        cur = 0
        suf = 0
        for i in range(n):
            cur += nums[i]
            suf += nums[n-i-1]
            prefix.append(cur)
            suffix.append(suf)
        suffix.reverse()
        for i in range(n):
            if prefix[i] == suffix[i]:
                return i
        else:
            return -1

