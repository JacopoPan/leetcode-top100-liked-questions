"""
Runtime: 41 ms, faster than 60.54% of Python3 online submissions for Fraction to Recurring Decimal.
Memory Usage: 14 MB, less than 77.00% of Python3 online submissions for Fraction to Recurring Decimal.
"""
from typing import List
from typing import Optional

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        ans = ''
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            ans += '-'
        if numerator < 0:
            numerator = -numerator
        if denominator < 0:
            denominator = -denominator
        resto = numerator
        history = []
        period = True
        while resto > 0:
            if resto < denominator:
                ans += '0'
                if period:
                    ans += '.'
                    period = False
                resto *= 10
            else:
                ans += str(resto // denominator)
                resto = resto%denominator
                if resto < denominator and resto != 0:
                    if period:
                        ans += '.'
                        period = False
                resto *= 10
            if resto in history:
                for idx in range(len(history)):
                    if history[idx] == resto:
                        i = len(history) - idx
                ans = ans[:len(ans)-i] +'(' + ans[len(ans)-i:] + ')'
                break
            history.append(resto)
        return ans

def main():
    sol = Solution()
    print('Output:', sol.fractionToDecimal(22, 7))
    print('Expected:', "3.(142857)")

if __name__ == "__main__":
    main()
