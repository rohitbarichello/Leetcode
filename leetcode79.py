def wordOnBoard(i, j, board, word, currLet, visited):
    if (i, j) not in visited:
        visited.add((i, j))
        
        if 0 <= i < len(board) and 0 <= j < len(board[0]):
            print(word[0:currLet] + board[i][j])
            print(i, j, currLet, visited)
            if board[i][j] == word[currLet]:
                if currLet + 1 == len(word):
                    return True
                else:
                    return (wordOnBoard(i + 1, j, board, word, currLet + 1, visited) or 
                            wordOnBoard(i - 1, j, board, word, currLet + 1, visited) or 
                            wordOnBoard(i, j + 1, board, word, currLet + 1, visited) or
                            wordOnBoard(i, j - 1, board, word, currLet + 1, visited))
            
            visited.remove((i,j))
            return False
                
    return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if(wordOnBoard(i, j, board, word, 0, set())):
                        return True
        
        return False