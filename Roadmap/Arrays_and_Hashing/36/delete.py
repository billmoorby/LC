import collections

class Solution:
  def isValidSudoku(self, board):
    N = 9
    row_map = collections.defaultdict(set)
    col_map = collections.defaultdict(set)
    square_map = collections.defaultdict(set)
  
    for r in range(N):
      for c in range(N):
        if board[r][c] == '.':
          continue

        if (board[r][c] in row_map[r] or 
            board[r][c] in col_map[c] or 
            board[r][c] in square_map[(r//3, c//3)]):
          return False
        
        row_map[r].add(board[r][c])
        col_map[c].add(board[r][c])
        square_map[(r//3, c//3)].add(board[r][c])
    
    return True
  