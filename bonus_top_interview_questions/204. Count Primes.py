"""
Runtime: 5834 ms, faster than 34.56% of Python3 online submissions for Count Primes.
Memory Usage: 52.7 MB, less than 85.70% of Python3 online submissions for Count Primes.
"""
from typing import List
from typing import Optional
import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [True] * n
        primes[0] = False
        primes[1] = False
        for i in range(2, int(math.sqrt(n)) + 1):
            if primes[i]:
                multiple = i**2
                while multiple < n:
                    primes[multiple] = False
                    multiple += i
        return sum(primes)

def main():
    sol = Solution()
    print('Output:', sol.countPrimes(10))
    print('Expected:', 4)

if __name__ == "__main__":
    main()
