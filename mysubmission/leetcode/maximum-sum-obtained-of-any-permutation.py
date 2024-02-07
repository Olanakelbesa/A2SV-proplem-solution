class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        MOD = 10**9 + 7
        freq = [0] * len(nums)

        for start, end in requests:
            freq[start] += 1
            if end + 1 < len(nums):
                freq[end + 1] -= 1

        for i in range(1, len(nums)):
            freq[i] += freq[i - 1]

        nums.sort(reverse=True)
        freq.sort(reverse=True)

        max_sum = sum(nums[i] * freq[i] for i in range(len(nums))) % MOD
        return max_sum

