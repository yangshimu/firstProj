class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])
        if rows == 0 or cols == 0: return False
        for r in range(rows):
            for c in range(cols):
                if self.existRecursive(board, r, c, 0, word):
                    return True
        return False

    def existRecursive(self, board, r, c, indx, word):
        if indx >= len(word): return True
        if r >= len(board) or c >= len(board[0]) or r < 0 or c < 0:
            return False
        if board[r][c] != word[indx]: return False
        temp = board[r][c]
        board[r][c] = "#"
        if self.existRecursive(board, r - 1, c, indx + 1, word):
            return True
        if self.existRecursive(board, r + 1, c, indx + 1, word):
            return True
        if self.existRecursive(board, r, c - 1, indx + 1, word):
            return True
        if self.existRecursive(board, r, c + 1, indx + 1, word):
            return True
        board[r][c] = temp
        return False


sot = Solution()
b=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
w="ABCB"
print(sot.exist(b,w))