class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perim = 0
    
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # up
                    if i == 0 or grid[i-1][j] == 0:                         # verify upper boundary or water
                        perim += 1
                    # down
                    if i == rows - 1 or grid[i+1][j] == 0:                  # verify lower boundary or water
                        perim += 1
                    # left
                    if j == 0 or grid[i][j-1] == 0:                         # verify left boundary or water
                        perim += 1
                    # right
                    if j == cols - 1 or grid[i][j+1] == 0:                  # verify right boundary or water
                        perim += 1
    
        return perim

# Time Complexity: O(m * n) where m is the number of rows and n is the number of columns in the grid.
# Space Complexity: O(1) as we are using a constant amount of extra space.