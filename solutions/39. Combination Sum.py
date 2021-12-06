"""
Runtime: 1116 ms, faster than 5.04% of Python3 online submissions for Combination Sum.
Memory Usage: 15.1 MB, less than 6.27% of Python3 online submissions for Combination Sum.
"""
from typing import List
from typing import Optional

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates = sorted(candidates)
        for i in candidates:
            if i > target:
                continue
            elif i == target:
                ret.append([i])
            else:
                lists = [[i]]
                while len(lists) > 0:
                    new_lists = []
                    for l in lists:
                        for j in range(0,len(candidates)):
                            temp_list = l + [candidates[j]]
                            temp_list = sorted(temp_list)
                            if sum(temp_list) == target:
                                if temp_list not in ret:
                                    ret.append(temp_list)
                            elif sum(temp_list) < target:
                                new_lists.append(temp_list)
                    lists = new_lists
        return ret

def main():
    sol = Solution()
    print('Output:', sol.combinationSum([2,3,6,7], 7))
    print('Expected:', [[2,2,3],[7]])

if __name__ == "__main__":
    main()
