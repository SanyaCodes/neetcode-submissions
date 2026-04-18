class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict

        hm_row = defaultdict(set)
        hm_col = defaultdict(set)
        hm_box = defaultdict(set)


        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] != ".":
                    if board[i][j] in hm_row[i]: return False
                    if board[i][j] not in hm_row[i]: hm_row[i].add(board[i][j]) 
                    
                    if board[i][j] in hm_col[j]: return False
                    if board[i][j] not in hm_col[j]: hm_col[j].add(board[i][j])

                    box_i = i//3
                    box_j = j//3

                    if board[i][j] in hm_box[str(i//3)+str(j//3)]: return False
                    if board[i][j] not in hm_box[str(i//3)+str(j//3)]: hm_box[str(i//3)+str(j//3)].add(board[i][j])

        return True



                

                
