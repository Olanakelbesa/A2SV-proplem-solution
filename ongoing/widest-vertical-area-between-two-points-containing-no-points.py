class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        n = len(points) 
        points.sort()
        max_i = 0
        for i in range(n - 1):
            max_i = max((points[i+1][0] - points[i][0]), max_i)
        return max_i

