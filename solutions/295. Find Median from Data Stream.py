"""
Runtime: 655 ms, faster than 68.01% of Python3 online submissions for Find Median from Data Stream.
Memory Usage: 36.5 MB, less than 13.49% of Python3 online submissions for Find Median from Data Stream.
"""
from typing import List
from typing import Optional
import heapq as hq

class MedianFinder:
 
    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:        
        hq.heappush(self.low, -num)
        hq.heappush(self.high, -hq.heappop(self.low))
        if len(self.high) > len(self.low):
            hq.heappush(self.low, -hq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0])/2

def main():
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    ans_1 = obj.findMedian()
    obj.addNum(3)
    ans_2 = obj.findMedian()
    print('Output:', ans_1, ans_2)
    print('Expected:', 1.5, 2)

if __name__ == "__main__":
    main()
