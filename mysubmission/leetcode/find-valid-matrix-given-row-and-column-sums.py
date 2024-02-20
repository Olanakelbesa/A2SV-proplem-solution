class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:  
        grid = []
        for i in range(len(rowSum)):
            grid.append([0]*len(colSum))
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                if rowSum[i] <= colSum[j]:
                    grid[i][j] = rowSum[i]
                    colSum[j] -= rowSum[i]
                    rowSum[i] -= rowSum[i]
                else:
                    grid[i][j] = colSum[j]
                    rowSum[i] -= colSum[j]
                    colSum[j] -= colSum[j]
        return grid
