class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        step, can = 0, capacity
        for i, plant in enumerate(plants):
            if can < plant:
                step += 2*i
                can = capacity
            step += 1
            can -= plant 
        return step
