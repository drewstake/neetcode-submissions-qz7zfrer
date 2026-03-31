class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])

        zero_col = set()
        zero_row = set()

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    zero_col.add(c)
                    zero_row.add(r)

        

        for r in range(row):
            for c in range(col):
                if r in zero_row or c in zero_col:
                    matrix[r][c] = 0
        
        
