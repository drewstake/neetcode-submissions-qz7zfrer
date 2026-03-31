class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    self.dfs(r,c,grid)
        

        return islands

    def dfs(self,r,c,grid):
        rows = len(grid)
        cols = len(grid[0])
        if c < 0 or c >= cols or r < 0 or r >= rows or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        self.dfs(r+1,c,grid) 
        self.dfs(r,c+1,grid)
        self.dfs(r-1,c,grid)
        self.dfs(r,c-1,grid)

    # Time O(n x m) where n = # rows and m = # columns
    # Space O(n x m) where n = # rows and m = # columns