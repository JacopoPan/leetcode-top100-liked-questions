"""
Runtime: 1650 ms, faster than 62.61% of Python3 online submissions for Word Search II.
Memory Usage: 15.6 MB, less than 70.61% of Python3 online submissions for Word Search II.
"""
from typing import List
from typing import Optional

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie={}
        for word in words:
            temp=trie
            for character in word:
                if character not in temp:
                    temp[character]={}
                temp=temp[character]
            temp['#']='#'
        self.res=[]
        self.rows = len(board)
        self.cols = len(board[0])
        for i in range(self.rows):
            for j in range(self.cols):
                self.find(board,i,j,trie,[])
        return self.res
    
    def find(self,board,i,j,trie,pre):
        if '#' in trie:
            del trie["#"]
            self.res.append(''.join(pre))
        if i<0 or i>=self.rows or j<0 or j>=self.cols:
            return
        if board[i][j] in trie:
            save_char = board[i][j]
            board[i][j] = '$'
            pre.append(save_char)
            self.find(board,i+1,j,trie[save_char],pre)
            self.find(board,i,j+1,trie[save_char],pre)
            self.find(board,i-1,j,trie[save_char],pre)
            self.find(board,i,j-1,trie[save_char],pre)
            board[i][j] = save_char
            pre.pop()
            if not trie[board[i][j]]:
                del trie[board[i][j]]

def main():
    sol = Solution()
    print('Output:', sol.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
    print('Expected:', ["oath","eat"])

if __name__ == "__main__":
    main()
