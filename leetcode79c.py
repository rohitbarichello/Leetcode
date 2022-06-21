class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def does_exist(k, r, c, s):
            if (r, c) in s:
                return False
            if not (0 <= r < row and 0 <= c < col):
                return False
            if not k:
                return board[r][c] == word[k]
            return (
                k
                and board[r][c] == word[k]
                and any(
                    map(
                        lambda x: does_exist(k - 1, *x, s | {(r, c)}),
                        ((r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)),
                    )
                )
            )

        seen, wl, row, col = set(), len(word), len(board), len(board[0])
        return any(
            does_exist(wl - 1, r, c, seen) for c in range(col) for r in range(row)
        )
