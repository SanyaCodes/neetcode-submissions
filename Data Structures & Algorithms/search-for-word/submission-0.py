class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
                        # up, down, right, left
        directions = [(-1,0), (1,0), (0,1), (0,-1)]

        m, n = len(board), len(board[0])

        visited = [[False for j in range(n)] for i in range(m)]

        def isValid(i, j):
            if i>=m or j>=n or i<0 or j<0:
                return False
            if visited[i][j]:
                return False
            return True
        
        def search(i, j, curr_len):
            if word[curr_len-1] != board[i][j]:
                return False
            if curr_len == len(word):
                return True
            for direc in directions:
                next_x, next_y = i+direc[0], j+direc[1]
                if isValid(next_x, next_y):
                    visited[next_x][next_y] = True
                    found = search(next_x, next_y, curr_len+1)
                    if found:
                        return True
                    visited[next_x][next_y] = False
            return False
        
        for i in range(m):
            for j in range(n):
                visited[i][j] = True
                found = search(i, j, 1)
                if found:
                    return True
                visited[i][j] = False
        return False

            
        
            





        