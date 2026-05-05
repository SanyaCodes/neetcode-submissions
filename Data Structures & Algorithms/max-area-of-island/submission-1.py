class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        areas = []
        visit = set()

        def bfs(r,c):
            que = collections.deque()
            que.append((r,c))
            visit.add((r,c))
            area = 1

            while que:
                r,c = que.popleft()
                d = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in d:
                    nr = r+dr
                    nc = c+dc
                    if (nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc] == 1 and
                        (nr,nc) not in visit):
                        area += 1
                        visit.add((nr,nc))
                        que.append((nr,nc))
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    # print(bfs(r,c))
                    areas.append(bfs(r,c))

        return max(areas) if areas else 0
