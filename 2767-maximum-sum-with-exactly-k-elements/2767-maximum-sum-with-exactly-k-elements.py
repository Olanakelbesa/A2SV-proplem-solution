class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        _max = max(nums) 
        ans = 0
        for _ in range(k):
            ans += _max
            _max += 1
        return ans

