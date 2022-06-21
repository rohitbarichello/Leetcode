def exist(self, g: List[List[str]], word: str) -> bool:
    R, C = len(g), len(g[0])

    def spread(i, j, w):
        if not w:
            return True
        original, g[i][j] = g[i][j], "-"
        spreaded = False
        for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if 0 <= x < R and 0 <= y < C and w[0] == g[x][y] and spread(x, y, w[1:]):
                spreaded = True
                break
        g[i][j] = original
        return spreaded

    for i in range(R):
        for j in range(C):
            if g[i][j] == word[0] and spread(i, j, word[1:]):
                return True
    return False
