class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrow = 1
        end = points[0][1]
        for i in range(len(points)):
            if points[i][0] > end:
                arrow += 1
                end = points[i][1]
            else:
                end = min(end, points[i][1])
        return arrow