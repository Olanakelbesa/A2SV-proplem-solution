class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        max_candie = max(candies)
        for candie in candies:
            sum_candie = 0
            sum_candie = extraCandies + candie
            if sum_candie >= max_candie:
                result.append(True)
            else:
                result.append(False)
        return result