class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        len_rows = len(grid)
        len_cols = len(grid[0])
        def dfs(w,h):
            #print(w,h, grid[0][0],grid[1][0],grid[0][1])
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                x,y = w+dx,h+dy
                if len_rows>x>-1 and len_cols>y>-1:
                    if grid[x][y] == "1":
                        grid[x][y] = "0"
                    else:
                        continue
                    dfs(x,y)
        n = 0
        for w in range(len_rows):
            for h in range(len_cols):
                if grid[w][h] == "1":
                    n+=1
                    dfs(w,h)
        return n