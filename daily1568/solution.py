class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        # function to count number of islands in grid
        def count_islands():
            visited = set()
            # function to run depth first search 
            def DepthFirstSearch(row, col):
                # initalize island node to search from 
                stack = [(row, col)]
                while stack: # while there are still nodes to serach
                    # grab grid position, removing from stack
                    x, y = stack.pop() 
                    for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                        if (0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1 and (nx, ny) not in visited):
                            visited.add((nx, ny))
                            stack.append((nx ,ny))
            # initialize islands variable to store count of islands
            islands = 0
            # loop through each point of the grid and check to see if it is a land cell
            # if it is land, recursively search through all connected nodes to see if there are any land connections
            # and store those nodes in visited
            # This way, connected land cells will only be counted as one island. 
            for i in range(len(grid)): # for each row
                for j in range(len(grid[0])): # for each column
                    if grid[i][j] == 1 and (i, j) not in visited:
                        islands += 1 # count new island
                        visited.add((i, j)) # add to set of visited nodes
                        # conduct depth first search to find all connected island nodes: 
                        DepthFirstSearch(i, j)
            return islands
        
        # if number of islands does not equal 1 to start, 
        # then grid is already disconnected, return 0 
        if count_islands() != 1: 
            return 0
        
        # see if the grid can be disconnected in one day (removing one land cell):
        for i in range(len(grid)): # for each row
            for j in range(len(grid[0])): # for each column
                if grid[i][j] == 1:
                    grid[i][j] = 0 # try removing the land node
                    if count_islands() != 1: # see if that disconnects the grid
                        return 1
                    grid[i][j] = 1 # set back to land node before iterating further

        # if the grid can not be disconnected in 1 day, 
        # then the maximum possible days it would take is 2
        return 2


# Test Cases: 
grid1 = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
# Expected: 2
Solution().minDays(grid = grid1)
# Output: 2

grid2 = [[1,1]]
# Expected: 2
Solution().minDays(grid = grid2)
# Output: 2