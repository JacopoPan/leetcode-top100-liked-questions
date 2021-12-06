"""
Runtime: 36 ms, faster than 26.38% of Python3 online submissions for Unique Paths.
Memory Usage: 14.2 MB, less than 66.78% of Python3 online submissions for Unique Paths.
"""
from typing import List
from typing import Optional

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        x_max = n-1
        y_max = m-1
        nodes_at_dist = [[0,0]]
        counters = [1]
        dist = x_max + y_max
        num_paths = 0
        d = 1
        while d <= dist + 1:
            temp = []
            temp_cnt = []
            if d == dist + 1:
                return counters[0]
            for n_idx, n in enumerate(nodes_at_dist):
                if n[0]+1 <= x_max:
                    nxt = [n[0]+1, n[1]]
                    if not nxt in temp:
                        temp.append(nxt)
                        temp_cnt.append(counters[n_idx])
                    else:
                        j = temp.index(nxt)
                        temp_cnt[j] += counters[n_idx]
                if n[1]+1 <= y_max:
                    nxt = [n[0], n[1]+1]
                    if not nxt in temp:
                        temp.append(nxt)
                        temp_cnt.append(counters[n_idx])
                    else:
                        j = temp.index(nxt)
                        temp_cnt[j] += counters[n_idx]
            nodes_at_dist = temp
            counters = temp_cnt
            d += 1

def main():
    sol = Solution()
    print('Output:', sol.uniquePaths(3,7))
    print('Expected:', 28)

if __name__ == "__main__":
    main()
