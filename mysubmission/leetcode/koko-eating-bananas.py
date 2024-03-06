class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def possible(k):
            cur_sum = 0
            for pile in piles:
                cur_sum += ceil(pile / k)
            return cur_sum <= h
        
        low, high = 1, max(piles)
        ans = 0
        while low <= high:
            mid = (high + low) // 2
            if possible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans 

