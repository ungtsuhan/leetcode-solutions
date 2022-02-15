"""
Date        : 15 Febuary 2022
Runtime     : 728 ms, faster than 92.15% of Python3 online submissions for 3Sum.
Memory Usage: 18.1 MB, less than 39.89% of Python3 online submissions for 3Sum.
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
        
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

import unittest

class threeSumCase(unittest.TestCase):
    def test_threeSum(self):
        func = Solution().threeSum
        self.assertEqual(func([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
        self.assertEqual(func([]), [])
        self.assertEqual(func([0]),[])
        self.assertEqual(func([0, 0, 0, 0]),[[0, 0, 0]])

if __name__ == '__main__':
    unittest.main()