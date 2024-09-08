class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int: 
        def isPossible(mid):
            day = 1
            summ = 0
            for w in weights:
                if summ + w > mid:
                    day += 1
                    summ = 0
                summ += w
            return day <= days

        low, high = max(weights), sum(weights)
        while low <= high:
            mid = (low + high) // 2
            if isPossible(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low



