class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        new_matrix = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            for j in range(m):
                new_matrix[j][i] = matrix[i][j]
        return new_matrix
            
