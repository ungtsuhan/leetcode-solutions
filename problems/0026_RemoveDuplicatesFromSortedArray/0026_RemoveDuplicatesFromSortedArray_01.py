'''
Date        : 15 Febuary 2022
Runtime     : 84 ms, faster than 91.61% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.6 MB, less than 78.24% of Python3 online submissions for Remove Duplicates from Sorted Array.
'''

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l

import unittest

class removeDuplicatesCase(unittest.TestCase):
    def test_removeDuplicates(self):
        func = Solution().removeDuplicates
        self.assertEqual(func([1,1,2]), 2)
        self.assertEqual(func([0,0,1,1,1,2,2,3,3,4]), 5)
        self.assertEqual(func([1,1,1,2,2,3]), 3)

if __name__ == '__main__':
    unittest.main()