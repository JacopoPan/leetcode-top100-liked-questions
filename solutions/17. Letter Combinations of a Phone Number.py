"""
Runtime: 32 ms, faster than 64.53% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14.1 MB, less than 86.61% of Python3 online submissions for Letter Combinations of a Phone Number.
"""
from typing import List
from typing import Optional

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = [[],
                   ['a', 'b', 'c'],
                   ['d', 'e', 'f'],
                   ['g', 'h', 'i'],
                   ['j', 'k', 'l'],
                   ['m', 'n', 'o'],
                   ['p', 'q', 'r', 's'],
                   ['t', 'u', 'v'],
                   ['w', 'x', 'y', 'z'],
                  ]
        digits_list = list(digits)
        output = []
        for idx, d in enumerate(digits_list):
            if len(output) == 0:
                for j in letters[int(d)-1]:
                    output.append(j)
            else:
                new_output = []
                for k in output:
                    for j in letters[int(d)-1]:
                        new_output.append(k+j) 
                output = new_output
        return output

def main():
    sol = Solution()
    print('Output:', sol.letterCombinations('23'))
    print('Expected:', ["ad","ae","af","bd","be","bf","cd","ce","cf"])

if __name__ == "__main__":
    main()
