"""
Runtime: 8116 ms, faster than 5.00% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.7 MB, less than 57.79% of Python3 online submissions for Group Anagrams.
"""
from typing import List
from typing import Optional

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        idx = []
        for i, s in enumerate(strs):
            sorted_strs.append(self.generateHash(s))
            idx.append(i)
        ret = []
        while len(idx) > 0:
            temp = [strs[idx[0]]]
            new_idx = []
            for q, i in enumerate(idx[1:]):
                if sorted_strs[idx[0]] == sorted_strs[i]:
                    temp.append(strs[i])
                else:
                    new_idx.append(i)
            idx = new_idx
            ret.append(temp)
        return ret

    def generateHash(self, string):
        prod = 1
        sum = 0
        for i in string:
            prod *=ord(i)
            sum +=ord(i)
        return prod + sum

def main():
    sol = Solution()
    print('Output:', sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print('Expected:', [["bat"],["nat","tan"],["ate","eat","tea"]])

if __name__ == "__main__":
    main()
