"""
Date        : 30 January 2022
Runtime     : 84 ms, faster than 21.52% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 14.1 MB, less than 95.49% of Python3 online submissions for Intersection of Two Arrays II.
"""

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        intersect = []
        
        for num in nums1:
            if num in count:
                count[num] = count[num] + 1
            else:
                count[num] = 1
        
        for num in nums2:
            if num in count and count[num] > 0:
                intersect.append(num)
                count[num] = count[num] - 1
        
        return intersect

import unittest

class intersectCase(unittest.TestCase):
    def test_intersect(self):
        func = Solution().intersect
        self.assertEqual(func([1,2,2,1], [2,2]), [2,2])
        self.assertEqual(func([4,9,5], [9,4,9,8,4]), [9,4])

if __name__ == '__main__':
    unittest.main()