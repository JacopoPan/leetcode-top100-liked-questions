"""
Runtime: 341 ms, faster than 63.77% of Python3 online submissions for Shuffle an Array.
Memory Usage: 19.6 MB, less than 94.64% of Python3 online submissions for Shuffle an Array.
"""
from typing import List
from typing import Optional
from random import randint

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bak = self.nums
        self.nums = self.shuffle()

    def reset(self) -> List[int]:
        return self.bak

    def shuffle(self) -> List[int]:
        ans = []
        indices = list(range(len(self.nums)))
        while indices:
            idx = randint(0,len(indices)-1)
            ans.append(self.bak[indices[idx]])
            indices.remove(indices[idx])
        return ans

def main():
    obj = Solution([1,2,3])
    ans_1 = obj.shuffle()
    ans_2 = obj.reset()
    ans_3 = obj.shuffle()
    print('Output:', [ans_1, ans_2, ans_3])
    print('Expected:', [[3,2,1],[1,2,3],[2,1,3]])

if __name__ == "__main__":
    main()
