class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        MAX_side = max(m,n)

        

        matrix = []
        for i in range(0,MAX_side):
            matrix.append([0]*MAX_side)
        #populate last row and col to 1
        matrix.pop()
        matrix.append([1]*MAX_side)
        for i in range(0,MAX_side):
            matrix[i][-1] = 1
        #print(matrix)
        """
        [0, 0, 1], 
        [0, 0, 1], 
        [1, 1, 1]]"""



        start_row = len(matrix) - 2 #1
        temp = 1
        start_col = len(matrix) - 2#1

        while matrix[0][0] == 0:

            matrix[start_row][start_col] = matrix[start_row+1][start_col] + matrix[start_row][start_col+1]

            start_col -=1 # move left
            if start_col == -1:
                start_row -=1
                start_col = len(matrix) - 2 # reset
        if m == n:
            return matrix[0][0]
        return matrix[-m][-n]

                # start at matrix(n-2)(n-2
"""
                [0, 2, 1], 
                [3, 2, 1], 
                [1, 1, 1]]
"""


        

        