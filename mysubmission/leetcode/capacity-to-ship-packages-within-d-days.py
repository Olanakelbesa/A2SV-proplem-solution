class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int: 
        
        def possible(mid):
            cur = 0
            day = 1
            for weight in weights:
                if cur + weight > mid:
                    day += 1
                    cur = 0
                cur += weight
            return day <= days

        low = max(weights)
        high = sum(weights)
        ans = 0
        
        while low <= high:
            mid = (high + low) // 2
            if possible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans