"""
Date        : 11 Febuary 2022
Runtime     : 1079 ms, faster than 37.47% of Python3 online submissions for Container With Most Water.
Memory Usage: 27.5 MB, less than 72.85% of Python3 online submissions for Container With Most Water.
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute Force Solution
        '''
        maxArea = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                curArea = min(height[i], height[j]) * (j-i)
                maxArea = max(maxArea, curArea)
        return maxArea
        '''
        
        # Linear Time Solution O(n)
        maxArea = 0
        l, r = 0, len(height) - 1
        
        while(l != r):
            curArea = min(height[l], height[r]) * (r-l)
            maxArea = max(maxArea, curArea)
            
            # shift the pointer which is lower height
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
                
        return maxArea

import unittest

class maxAreaCase(unittest.TestCase):
    def test_maxArea(self):
        func = Solution().maxArea
        self.assertEqual(func([1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(func([1,1]), 1)

if __name__ == "__main__":
    unittest.main()