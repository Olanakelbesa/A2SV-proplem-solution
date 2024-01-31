class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        left, right, maxScore, currScore = 0, 0, 0, 0
        elements = set()
        while right < len(nums):
            while nums[right] in elements:
                elements.remove(nums[left])
                currScore -= nums[left]
                left += 1

            currScore += nums[right]
            elements.add(nums[right])
            maxScore = max(currScore, maxScore)
            right += 1

        return maxScore