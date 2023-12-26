class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sum_diagonal = 0
        for i in range(n):
            for j in range(len(mat[0])):
                if (i-j) == 0:
                    sum_diagonal += mat[i][j]
                    print(mat[i][j])
                if (i + j) == n - 1 and (i != j):
                    sum_diagonal += mat[i][j]
                    print(mat[i][j])

        return sum_diagonal 
        