"""
Runtime: 332 ms, faster than 5.13% of Python3 online submissions for Partition Labels.
Memory Usage: 14.4 MB, less than 26.01% of Python3 online submissions for Partition Labels.
"""
from typing import List
from typing import Optional

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ret = []
        part_idx = 1
        counter = part_idx
        while part_idx < len(s):
            looked = s[:part_idx]
            looking = s[part_idx:]
            if self.contains(looked, looking):
                pass
            else:
                ret.append(counter)
                counter = 0
            part_idx += 1
            counter += 1
        ret.append(counter)
        return ret

    def contains(self, looked: List[int], looking: List[int]) -> bool:
        for i in looked:
            if i in looking:
                return True
        return False

def main():
    sol = Solution()
    print('Output:', sol.partitionLabels("ababcbacadefegdehijhklij"))
    print('Expected:', [9,7,8])

if __name__ == "__main__":
    main()
