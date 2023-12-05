class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        a = min(start, destination)
        b = max(start, destination)

        return min(sum(distance[a:b]), sum(distance)-sum(distance[a:b]))
        
          
