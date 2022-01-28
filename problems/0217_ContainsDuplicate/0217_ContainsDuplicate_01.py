'''
Date        : 28 January 2022
Runtime     : 787 ms, faster than 12.24% of Python3 online submissions for Contains Duplicate.
Memory Usage: 25.9 MB, less than 51.51% of Python3 online submissions for Contains Duplicate.
'''

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap:
                return True
            else:
                hashMap[nums[i]] = i
        return False

# Unit Test
import unittest
class ContainsDuplicate(unittest.TestCase):
    def test_containsDuplicate(self):
        func = Solution().containsDuplicate
        self.assertEqual(func([1,2,3,1]), True)
        self.assertEqual(func([1,2,3,4]), False)
        self.assertEqual(func([1,1,1,3,3,4,3,2,4,2]), True)

if __name__ == '__main__':
    unittest.main()