class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistributed(mid):
            cnt = 0
            for num in quantities:
                cnt += ceil(num / mid)
            return cnt <= n
            

        l, r = 1, max(quantities)
        while l <= r:
            mid = (l+r) // 2
            if canDistributed(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l