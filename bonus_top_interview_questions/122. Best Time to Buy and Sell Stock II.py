"""
Runtime: 102 ms, faster than 33.65% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 15.2 MB, less than 67.52% of Python3 online submissions for Best Time to Buy and Sell Stock II.
"""
from typing import List
from typing import Optional

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = 0
        for idx in range(1,len(prices)):
            if prices[idx] > prices[idx-1]:
                profits += prices[idx]-prices[idx-1]   
        return profits

def main():
    sol = Solution()
    print('Output:', sol.maxProfit([7,1,5,3,6,4]))
    print('Expected:', 7)

if __name__ == "__main__":
    main()
