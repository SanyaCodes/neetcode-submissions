class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # create bfs function to mark all neighboring 1s as seen
        # send UNseen 1s into bfs and increment count each time sent
        # create isValid function to check each coordinate
        

        d = [[1,0],[-1,0],[0,1],[0,-1]]
        seen = set()
        m = len(grid)
        n = len(grid[0])
        count = 0

        def isvalid(x,y):
            if 0<=x<m and 0<=y<n:
                return True

        def bfs(r,c,seen):
            que = []
            que.append((r,c))
            while que:
                x,y = que.pop()
                for dx,dy in d:
                    nx,ny = x+dx,y+dy
                    if isvalid(nx,ny) and grid[nx][ny]=="1" and (nx,ny) not in seen:
                        seen.add((nx,ny))
                        que.append((nx,ny))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and (i,j) not in seen:
                    count += 1
                    bfs(i,j,seen)
        
        return count
            


            


        