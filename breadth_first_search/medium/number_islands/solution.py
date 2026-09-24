from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        islands = 0 

        def bfs(r, c): 
            q = deque([(r,c)])
            seen.add((r,c))

            while q:
                r, c = q.popleft()
                for dr, dc in [(0, 1), (0,-1), (1,0), (-1,0)]: 
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols 
                        and (nr, nc) not in seen and grid[nr][nc] == "1"):
                        seen.add((nr,nc))
                        q.append((nr,nc))

        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j] == "1" and (i,j) not in seen: 
                    bfs(i,j)
                    islands += 1
        return islands


# Test
grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
# Expected: 1
print(Solution().numIslands(grid1))
# Output: 

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# Expected: 3
print(Solution().numIslands(grid2))
# Output: 