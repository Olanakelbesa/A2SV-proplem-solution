class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        nums=[]
        for i in range(len(points)):
            d=(points[i][0]**2)+(points[i][1]**2)
            nums.append([d, points[i]])
        nums.sort(key=lambda x: x[0])

        k_smallest_points = [point[1] for point in nums[:k]]

        return(k_smallest_points)

            
        