class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        a = []
        for x in range(len(nums)):
            if nums[x] % 2:
                a.append(x)

        if len(a) < k:
            return 0

        a.append(len(nums))
        ans = (a[0] + 1) * (a[k] - a[k - 1])
        for x in range(1, len(a) - k):
            ans += (a[x] - a[x - 1]) * (a[x + k] - a[x + k - 1])
        
        return ans