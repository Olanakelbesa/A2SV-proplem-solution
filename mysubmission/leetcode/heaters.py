class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        max_diff = float("-inf")
        for house in houses:
            low, high = 0, len(heaters) - 1
            closest = float("inf")

            while low <= high:
                mid = (low + high) // 2
                if heaters[mid] > house:
                    closest = min(closest, abs(heaters[mid] - house))
                    high = mid - 1
                else:
                    closest = min(closest, abs(heaters[mid] - house))
                    low = mid + 1
            max_diff = max(closest, max_diff)
        return max_diff
