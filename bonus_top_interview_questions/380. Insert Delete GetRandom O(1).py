"""
Runtime: 544 ms, faster than 60.84% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 61.1 MB, less than 89.71% of Python3 online submissions for Insert Delete GetRandom O(1).
"""
from typing import List
from typing import Optional
from random import randint

class RandomizedSet:
    def __init__(self):
        self.val_set = {}
        self.keys = []
        self.length = 0

    def insert(self, val: int) -> bool:
        ret = True
        if val in self.val_set.keys():
            ret = False
        else:
            self.length += 1
            self.keys.append(val)
        self.val_set[val] = val
        return ret

    def remove(self, val: int) -> bool:
        ret = False
        if val in self.val_set.keys():
            ret = True
            del self.val_set[val]
            self.keys.remove(val)
            self.length -= 1
        return ret

    def getRandom(self) -> int:
        pick = randint(0,self.length-1)
        return self.val_set[self.keys[pick]]

def main():
    obj = RandomizedSet()
    ret_1 = obj.insert(1)
    ret_2 = obj.remove(2)
    ret_3 = obj.insert(2)
    ret_4 = obj.getRandom()
    ret_5 = obj.remove(1)
    ret_6 = obj.insert(2)
    ret_7 = obj.getRandom()
    print('Output:', [ret_1, ret_2, ret_3, ret_4, ret_5, ret_6, ret_7])
    print('Expected:', [True,False,True,2,True,False,2])

if __name__ == "__main__":
    main()
