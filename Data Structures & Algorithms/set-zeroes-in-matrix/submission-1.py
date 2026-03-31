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
        
        
# We are creating space for col set and row set so the space complexity would be O(r + c)
# The time complexity is that we are iterating through the matrix twice so it would be O(2 *(r*c)) which simplifies to O(r*c),
# We drop constant factors in Big-O because they don’t change how runtime grows with input size. O(2*r*c) simplifies to O(r*c).