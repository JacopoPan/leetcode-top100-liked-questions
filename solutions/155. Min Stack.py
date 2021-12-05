"""
Runtime: 60 ms, faster than 81.76% of Python3 online submissions for Min Stack.
Memory Usage: 17.9 MB, less than 98.52% of Python3 online submissions for Min Stack.
"""
from typing import List
from typing import Optional

class MinStack:

    def __init__(self):
        self.data = []
        self.num_data = 0
        self.min = None

    def push(self, val: int) -> None:
        self.data.append(val)
        if self.min == None:
            self.min = val
        elif val < self.min:
            self.min = val

    def pop(self) -> None:
        temp1 = self.data[0:self.num_data-1]
        temp2 = self.data[self.num_data-1]
        self.data = temp1
        new_min = None
        if temp2 == self.min:
            for i in range(len(temp1)):
                if new_min == None:
                    new_min = temp1[i]
                elif temp1[i] < new_min:
                    new_min = temp1[i]
            self.min = new_min

    def top(self) -> int:
        return self.data[self.num_data-1]

    def getMin(self) -> int:
        return self.min

def main():
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print('Output:', [obj.getMin(), obj.pop(), obj.top(), obj.getMin()])
    print('Expected:', [-3, None, 0, -2])

if __name__ == "__main__":
    main()
