"""
Date        : 10 Febuary 2022
Runtime     : 92 ms, faster than 85.42% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.3 MB, less than 82.98% of Python3 online submissions for Median of Two Sorted Arrays.
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        partitionSizeAB = (total + 1) // 2
        
        # ensure A is the shorter array, so that apply binary search on A (shorter array)
        if len(B) < len(A):
            A, B = B, A

        low, high = 0, len(A)
        while low <= high: 
            # partitioning arrays
            partitionSizeA = mid = (low + high) // 2
            partitionSizeB = partitionSizeAB - partitionSizeA
            
            # from partition size, determine the value for comparision
            Aleft  = A[partitionSizeA - 1]  if partitionSizeA - 1 >= 0  else float("-infinity")
            Aright = A[partitionSizeA]      if partitionSizeA < len(A)  else float("infinity")
            Bleft  = B[partitionSizeB - 1]  if partitionSizeB - 1 >= 0  else float("-infinity")
            Bright = B[partitionSizeB]      if partitionSizeB < len(B)  else float("infinity")
            
            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # even
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                # odd
                else:
                    return max(Aleft, Bleft)

            # parition not correct
            elif Aleft > Bright:
                high = mid - 1
            else:
                low  = mid + 1

import unittest

class findMedianSortedArraysCase(unittest.TestCase):
    def test_findMedianSortedArrays(self):
        func = Solution().findMedianSortedArrays
        self.assertEqual(func([1, 3], [2]), 2.0)
        self.assertEqual(func([1, 2], [3, 4]), 2.5)

if __name__ == '__main__':
    unittest.main()