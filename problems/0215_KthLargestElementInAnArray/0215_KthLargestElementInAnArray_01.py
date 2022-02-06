"""
Date        : 6 Febuary 2022
Runtime     : 98 ms, faster than 46.76% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 14.7 MB, less than 96.71% of Python3 online submissions for Kth Largest Element in an Array.
"""

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [-elem for elem in nums]
        heapq.heapify(arr)
        for i in range(k - 1):
            heapq.heappop(arr)
        return -heapq.heappop(arr)

import unittest

class findKthLargestCase(unittest.TestCase):
    def test_findKthLargest(self):
        func = Solution().findKthLargest
        self.assertEqual(func([3,2,1,5,6,4], 2), 5)
        self.assertEqual(func([3,2,3,1,2,4,5,5,6], 4), 4)

if __name__ == "__main__":
    unittest.main()