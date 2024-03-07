class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def possible(k):
            cur_sum = 0
            for num in nums:
                cur_sum += ceil(num / k)
            return cur_sum <= threshold
        
        low, high = 1, max(nums)
        ans = 0
        while low <= high:
            mid = (high + low) // 2
            if possible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans 