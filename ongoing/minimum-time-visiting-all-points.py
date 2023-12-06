class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sum_distance = 0
        for i in range(1, len(points)):
            hor = abs(points[i][0] - points[i-1][0])
            ver = abs(points[i][1] - points[i-1][1])
            sum_distance += max(hor, ver)
        return sum_distance