class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        totalA = 0
        diffB = [0]*n
        for i in range(n):
            totalA += costs[i][0]
        for i in range(n):
            diffB[i] =  costs[i][1] - costs[i][0]
        diffB.sort()
        for i in range((n//2)):
            totalA += diffB[i]
        return totalA