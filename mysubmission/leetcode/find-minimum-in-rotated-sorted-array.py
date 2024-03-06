class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if (mid + 1) < len(nums) and nums[mid + 1] < nums[mid]:
                    return nums[mid + 1]
            elif (mid - 1) > -1 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[-1] < nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return nums[0]

        
