class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        matrix_new=[[0]* r for _ in range(r)]
        for i in range(r):
            for j in range(r):
                matrix_new[j][r-i-1]=matrix[i][j]

        matrix[:] = matrix_new
