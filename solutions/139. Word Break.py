"""
Runtime: 48 ms, faster than 68.93% of Python3 online submissions for Word Break.
Memory Usage: 14 MB, less than 83.01% of Python3 online submissions for Word Break.
"""
from typing import List
from typing import Optional

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        breakable_up_to_idx = [True]
        for i in range(len(s)):
            appendable_word_to_breakable_str = False
            for j in range(i+1):
                if (breakable_up_to_idx[j] == True) and (s[j:i+1] in wordDict):
                    appendable_word_to_breakable_str = True
            if appendable_word_to_breakable_str:
                breakable_up_to_idx.append(True)
            else:
                breakable_up_to_idx.append(False)
        return breakable_up_to_idx[len(s)]

def main():
    sol = Solution()
    print('Output:', sol.wordBreak("leetcode", ["leet","code"]))
    print('Expected:', True)

if __name__ == "__main__":
    main()
