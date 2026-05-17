class Solution(object):
    def exist(self, board, word):

        from collections import Counter

        board_count = Counter(sum(board, []))
        word_count = Counter(word)

        for c in word_count:
            if board_count[c] < word_count[c]:
                return False

        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        rows, cols = len(board), len(board[0])

        def backtrack(r, c, k = 0):

            if k == len(word):
                return True

            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False

            if board[r][c] != word[k]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            res = (
                backtrack(r+1,c,k+1) or
                backtrack(r-1,c,k+1) or
                backtrack(r,c+1,k+1) or
                backtrack(r,c-1,k+1)
            )

            board[r][c] = temp
            return res

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if backtrack(i,j):
                        return True

        return False
