"""
Runtime: 32 ms, faster than 87.26% of Python3 online submissions for Word Break II.
Memory Usage: 13.9 MB, less than 83.97% of Python3 online submissions for Word Break II.
"""
from typing import List
from typing import Optional

class Solution:
    def __init__(self):
        self.cache = {}
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if s in self.cache.keys():
            return self.cache[s]
        if len(s)==0:
            return []
        ans = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                ans.append(word)
            else:
                all_possible_splits = self.wordBreak(s[len(word):], wordDict)
                for elem in all_possible_splits:
                    elem = word + ' ' + elem
                    ans.append(elem)
        self.cache[s] = ans
        return ans

def main():
    sol = Solution()
    print('Output:', sol.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))
    print('Expected:', ["cats and dog","cat sand dog"])

if __name__ == "__main__":
    main()
