class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r=len(matrix)
        l=len(matrix[0])
        row=[]
        column=[]
        for i in range(r):
            for j in range(l):
                if matrix[i][j]==0:
                    if i not in row:
                        row.append(i)
                    if j not in column:
                        column.append(j)
        for m in row:
            for x in range(l):    
                matrix[m][x]=0
        for n in column:
            for y in range(r):
                matrix[y][n]=0
