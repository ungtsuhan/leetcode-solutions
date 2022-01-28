'''
Date        : 29 January 2022
Runtime     : 1187 ms, faster than 21.34% of Python3 online submissions for Maximum Subarray.
Memory Usage: 27.9 MB, less than 97.79% of Python3 online submissions for Maximum Subarray.
'''

from typing import List

class Solution:

    # Algoritm: Kadane's Algorithm
    # Time Complexity: O(n)

    def maxSubArray(self, nums: List[int]) -> int:
        
        currentSum, globalSum = 0, 0
        
        for i in range(len(nums)):
            if i == 0:
                currentSum = nums[i]
                globalSum = nums[i]
            else:
                if nums[i] > currentSum + nums[i]:
                    currentSum = nums[i]
                else:
                    currentSum += nums[i]
                    
                if globalSum < currentSum:
                    globalSum = currentSum
                    
        return globalSum

# Unit Test
import unittest
class MaxSubArray(unittest.TestCase):
    def test_maxSubArray(self):
        func = Solution().maxSubArray
        self.assertEqual(func([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(func([1]), 1)
        self.assertEqual(func([5,4,-1,7,8]), 23)

if __name__ == '__main__':
    unittest.main()