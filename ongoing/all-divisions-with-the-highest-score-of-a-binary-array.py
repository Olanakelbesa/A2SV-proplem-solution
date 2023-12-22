class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        count_1 = 0
        for num in nums:
            if num == 1: count_1 += 1

        count_0, max_div = 0, count_1
        d = defaultdict(list)
        d[count_1].append(0)
        for i, num in enumerate(nums):
            count_0 += int(num == 0)
            count_1 -= int(num == 1)
            d[count_0 + count_1].append(i + 1)
            max_div = max(max_div, count_0 + count_1)
        return d[max_div]
