class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        l = 0
        maxSum = 0
        windowSum = 0
        for r in range(len(nums)):
            cnt[nums[r]] += 1
            windowSum += nums[r]

            if r - l + 1 > k:
                cnt[nums[l]] -= 1
                if cnt[nums[l]] == 0:
                    del cnt[nums[l]]
                windowSum -= nums[l]
                l += 1

            if r - l + 1 == k and len(cnt) == k:
                maxSum = max(maxSum, windowSum)
                
        return maxSum



