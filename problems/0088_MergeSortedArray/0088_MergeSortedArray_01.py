"""
Date        : 29 January 2022
Runtime     : 70 ms, faster than 9.78% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14.1 MB, less than 95.56% of Python3 online submissions for Merge Sorted Array.
"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        i, j, k = m-1, n-1, len(nums1)-1
        
        while(k >= 0):
            if(i >= 0 and j >= 0 and nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                i-=1
            elif (i >= 0 and j >= 0 and nums1[i] <= nums2[j]):
                nums1[k] = nums2[j]
                j-=1
            elif i < 0:
                nums1[k] = nums2[j]
                j-=1
            elif j < 0:
                nums1[k] = nums1[i]
                i-=1
            k-=1
            
        return nums1

# Unit Test
import unittest

class Merge(unittest.TestCase):
    def test_merge(self):
        func = Solution().merge
        self.assertEqual(func([1,2,3,0,0,0], 3, [2,5,6], 3), [1,2,2,3,5,6])
        self.assertEqual(func([1], 1, [], 0), [1])
        self.assertEqual(func([0], 0, [1], 1), [1])

if __name__ == '__main__':
    unittest.main()