"""
Runtime: 1024 ms, faster than 72.93% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25.2 MB, less than 54.94% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
from typing import List
from typing import Optional

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        best_future_sell = prices[len(prices)-1]
        for idx in range(len(prices)-1):
            current_buying_price = prices[len(prices)-2-idx]
            profit = best_future_sell - current_buying_price
            if profit > max_profit:
                max_profit = profit
            if current_buying_price > best_future_sell:
                best_future_sell = current_buying_price
        return max_profit

def main():
    sol = Solution()
    print('Output:', sol.maxProfit([7,1,5,3,6,4]))
    print('Expected:', 5)

if __name__ == "__main__":
    main()
