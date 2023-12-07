class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        myset = set()
        for i in range(len(ranges)):
            first = ranges[i][0]
            second = ranges[i][1]

            for j in range(first, second+1):
                myset.add(j)
        print(myset)
        for num in range(left, right+1):
            if num not in myset:
                return False
        return True