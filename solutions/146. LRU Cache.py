"""
Runtime: 5452 ms, faster than 5.00% of Python3 online submissions for LRU Cache.
Memory Usage: 75.2 MB, less than 76.44% of Python3 online submissions for LRU Cache.
"""
from typing import List
from typing import Optional

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used = 0
        self.cache = {}
        self.age = {}
        self.time = 0

    def get(self, key: int) -> int:
        self.time += 1
        ans = -1
        if key in self.cache.keys():
            self.age[key] = self.time
            ans = self.cache[key]
        return ans

    def put(self, key: int, value: int) -> None:
        self.time += 1
        if key not in self.cache.keys():
            if self.used == self.capacity:
                oldest_key = min(self.age, key=self.age.get)
                self.cache.pop(oldest_key)
                self.age.pop(oldest_key)
            else:
                self.used += 1
        self.cache[key] = value
        self.age[key] = self.time

def main():
    ans = []
    cache = LRUCache(2)
    cache.put(1,1)
    cache.put(2,2)
    ans.append(cache.get(1))
    cache.put(3,3)
    ans.append(cache.get(2))
    cache.put(4,4)
    ans.append(cache.get(1))
    ans.append(cache.get(3))
    ans.append(cache.get(4))
    print('Output:', ans)
    print('Expected:', [1,-1,-1,3,4])

if __name__ == "__main__":
    main()
