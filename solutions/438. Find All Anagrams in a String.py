"""
Runtime: 204 ms, faster than 55.01% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 15.5 MB, less than 6.71% of Python3 online submissions for Find All Anagrams in a String.
"""
from typing import List
from typing import Optional

class Solution:
    def __init__(self):
        self.cache = {}
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        for ch in p:
            if ch in self.cache.keys():
                self.cache[ch] += 1
            else:
                self.cache[ch] = 1
        ans = []
        for i in range(len(s)-len(p)+1):
            if i == 0:
                for ch in s[i:i+len(p)]:
                     if ch in self.cache.keys():
                        self.cache[ch] -= 1
            else:
                if s[i-1] in self.cache.keys():
                    self.cache[s[i-1]] += 1
                if s[i+len(p)-1] in self.cache.keys():
                    self.cache[s[i+len(p)-1]] -= 1    
            if self.check():
                ans.append(i)
        return ans
    
    def check(self) -> bool:
        if all(v==0 for v in self.cache.values()):
            return True
        return False

def main():
    sol = Solution()
    print('Output:', sol.findAnagrams("cbaebabacd", "abc"))
    print('Expected:', [0, 6])

if __name__ == "__main__":
    main()