"""
Runtime: 161 ms, faster than 82.67% of Python3 online submissions for Word Ladder.
Memory Usage: 17.5 MB, less than 46.26% of Python3 online submissions for Word Ladder.
"""
from typing import List
from typing import Optional
from collections import defaultdict
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or len(endWord)==0 or len(beginWord)==0 or len(wordList)==0:
            return 0
        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word) 
        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        while len(queue)>0:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
        return 0

def main():
    sol = Solution()
    print('Output:', sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
    print('Expected:', 5)

if __name__ == "__main__":
    main()
