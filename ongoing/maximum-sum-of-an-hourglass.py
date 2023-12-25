class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def maxSum(i, j) :
            return sum(grid[i-1][j-1:j+2]) + grid[i][j] + sum(grid[i+1][j-1: j+2])

        row = len(grid)
        col = len(grid[0])

        best_sum = 0
        for i in range(1, row-1):
            for j in range(1, col-1):
                best_sum = max(best_sum, maxSum(i, j))
        return best_sum