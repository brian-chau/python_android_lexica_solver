class Solution:
    def backtrack_exist(self, board, x, y, word, k):
        if k == len(word):
            return True
        if not (0 <= x < len(board) and 0 <= y < len(board[0])):
            return False

        if board[x][y] != word[k]:
            return False

        board[x][y] = ord(board[x][y]) ^ 256
        exist = any(
            (
                self.backtrack_exist(board, x,     y + 1, word, k + 1),
                self.backtrack_exist(board, x,     y - 1, word, k + 1),
                self.backtrack_exist(board, x + 1, y,     word, k + 1),
                self.backtrack_exist(board, x - 1, y,     word, k + 1),
                self.backtrack_exist(board, x + 1, y + 1, word, k + 1),
                self.backtrack_exist(board, x - 1, y + 1, word, k + 1),
                self.backtrack_exist(board, x + 1, y - 1, word, k + 1),
                self.backtrack_exist(board, x - 1, y - 1, word, k + 1)
            )
        )
        board[x][y] = chr(board[x][y] ^ 256)
        return exist

    def exist(self, board, word) -> bool:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                exist = self.backtrack_exist(board, i, j, word, 0)
                if not exist:
                    continue
                return exist

        return False


if __name__ == '__main__':
    obj = Solution()

    with open('board.txt') as f:
        board = [list(line.lower().strip()) for line in f.readlines()]

    with open('words.txt') as f:
        words = [line.lower().strip() for line in f.readlines()]

    with open('output.txt', 'w+') as f:
        results = []
        for word in words:
            if obj.exist(board, word) and len(word) >= 3:
                results.append(word)
        results.sort(key=len, reverse=True)
        for word in results:
            f.write(word + '\n')
