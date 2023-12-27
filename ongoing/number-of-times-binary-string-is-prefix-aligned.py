class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_i = flips[0]
        count_i = 0
        for i in range(len(flips)):
            max_i = max(flips[i], max_i)
            if max_i == i+1:
                count_i += 1
        return count_i