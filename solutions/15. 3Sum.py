"""
Runtime: 1444 ms, faster than 39.82% of Python3 online submissions for 3Sum.
Memory Usage: 17.4 MB, less than 73.99% of Python3 online submissions for 3Sum.
"""
from typing import List
from typing import Optional

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            if i != 0 and nums[i] == nums[i-1]:
                continue
            else:
                while j < k:
                    if (k != len(nums)-1) and (nums[k] == nums[k+1]):
                        k -= 1
                    elif (nums[i] + nums[j] + nums[k]) > 0:
                        k -= 1
                    elif (nums[i] + nums[j] + nums[k]) < 0:
                        j += 1
                    else:
                        ans.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
        return ans
def main():
    sol = Solution()
    print('Output:', sol.threeSum([-1,0,1,2,-1,-4]))
    print('Expected:', [[-1,-1,2],[-1,0,1]])

if __name__ == "__main__":
    main()
