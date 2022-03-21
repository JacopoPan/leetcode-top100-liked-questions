"""
Runtime: 2208 ms, faster than 38.39% of Python3 online submissions for Coin Change.
Memory Usage: 14.1 MB, less than 69.45% of Python3 online submissions for Coin Change.
"""
from typing import List
from typing import Optional
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_coins = [0] + [math.inf for i in range(amount)]
        for target_val in range(1, amount+1):
            for coin_val in coins:
                if target_val - coin_val >= 0:
                    num_coins[target_val] = min(num_coins[target_val], num_coins[target_val-coin_val] + 1)
        if num_coins[-1] == math.inf:
            return -1
        else:
            return num_coins[-1]

def main():
    sol = Solution()
    print('Output:', sol.coinChange([1,2,5], 11))
    print('Expected:', 3)

if __name__ == "__main__":
    main()
