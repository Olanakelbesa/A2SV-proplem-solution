class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) -1
        first = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            if target >  nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                first = mid
                high = mid -1

        low, high = 0, len(nums) -1
        last = -1
        while low <= high:
            mid = low + (high - low) // 2
            if target >  nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                last = mid
                low = mid + 1

        return [first, last]

#5 7 7 8 8 10
#0 1 2 3 4 5
#      ^
#
#mid = 2
